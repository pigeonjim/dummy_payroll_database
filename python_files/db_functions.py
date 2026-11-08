import psycopg, getpass, json
from psycopg import sql

class dataBaseLogins:
    """ class to get db connection information from end user
    - tests connection
    - provides connection string for other classes
    """
    def __init__(self):
        self.get_logins()

    @property
    def db_name(self):
        return self.__db_namer
    def db_name(self):
        self.__db_name = input("Please input the database name: ")

    @property
    def user(self):
        return self.__user
    def user(self):
        self.__user = input("Please input the database username: ")

    @property
    def pword(self):
        #may need removing
        return self.__pword
    def pword(self):
        self.__pword = getpass.getpass("Please input the password: ")

    def get_logins(self):
        self.db_name()
        self.user()
        self.pword()
        self.test_logins()

    def connection_string(self):
        return (f"""dbname={self.__db_name} user={self.__user} password={self.__pword}""")

    def test_logins(self):
        try:
            with psycopg.connect(self.connection_string()) as connection:
                pass
        except psycopg.OperationalError:
            print("connection error")
            print(self)
            choice = input("Would like like to reinput the login details Y or N?")
            if choice.upper() == 'Y':
                self.get_logins()

    def __str__(self):
        return (f"Current database dbname = {self.__db_name} and username = {self.__user}")

class checkDbTables:
    """Class for methods that check the current state of the database
    - checks if all the required tables present"""

    #class atribute - a list of the required table names
    list_of_tbls = ["payroll_runs", "employee", "ee_jobs", "employer", "payslips", "deductions"
            , "deduction_config", "frequency", "payments", "payment_config", "office"]
    
    def __init__(self):
        self.__tbls = {}

    def get_current_tbls(self, db_logins: dataBaseLogins):
        missing_tbls = []
        with psycopg.connect(db_logins.connection_string()) as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';""")
                
                for record in cur:
                    print(record[0])

class buildDbJSON:
    """ code to build JSON files that show the required database tables
        there tables are for configuration and to aid processing
        each table is a seperate JSON file
        each JSON files shows the field names and types
    """
    def __init__(self):
        self.data_path = "../db_JSON_files"
        self.tbls = {}

    def loadtbls(self, db_logins: dataBaseLogins):
        with psycopg.connect(db_logins.connection_string()) as conn:
            with conn.cursor() as cur:
                #first cursor to get table names
                cur.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';""")
                for record in cur:
                    self.tbls[record[0]] = None
                #get field names and types for each table
                for key in self.tbls:
                    new_dict = {}
                    qry = sql.SQL("SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = {what_tbl};"
                                  ).format(what_tbl = key)
                    cur.execute(qry)
                    for result in cur:
                        new_dict[result[0]] = result[1]
                    self.tbls[key] = new_dict
        for key, tbl in self.tbls.items():
            path = (f'../db_JSON_files/{key}')
            print(path)
            with open(path,"w") as jfile:
                json.dump(tbl, jfile,indent=4)


