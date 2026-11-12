import psycopg, getpass, json, os
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

class whatsInTheBox:
    """class that queries the database to get current schema
    - This is processed in a dictionary of dictionaries where
    1. top level key key is a table name
    2. second level is of the config  key = field name : value = field type
    """
    def __init__(self):
        pass

    def whats_in_the_box(self, db_logins: dataBaseLogins):
        current_schema = {}
        with psycopg.connect(db_logins.connection_string()) as conn:
            with conn.cursor() as cur:
                #first cursor to get table names
                cur.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';""")
                for record in cur:
                    current_schema[record[0]] = None
                #get field names and types for each table
                for key in current_schema:
                    new_dict = {} 
                    qry = sql.SQL("SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = {what_tbl};"
                                  ).format(what_tbl = key)
                    cur.execute(qry)
                #populate dictionaries
                    for result in cur:
                        new_dict[result[0]] = result[1]
                    current_schema[key] = new_dict
        return current_schema

    @property
    def current_schema(self):
        return self.__current_schema

class checkDbTables:
    """Class that checks the current schema of the database
    - checks if all the required tables and fields are present
    - checks db fields are of the correct type"""
    
    def __init__(self, path: str):
       """
            path = the path to the JSON folder
       """
       self.data_path = path
       self.tbl_dicts = self.read_tblJSON()

    def read_tblJSON(self):
        """
        JSON files processed in a dictionary of dictionaries where
        1. top level key key is a table name
        2. second level is of the config  key = field name : value = field type
        """
        tbl_list = {}
        for tbl in os.listdir(self.data_path):
            path = (f"{self.data_path}/{tbl}")
            with open(path,'r') as tbl_file:
                tbl_list[tbl.replace('.JSON','')] = json.load(tbl_file)
        return tbl_list



    def check_tables(self, curnt_tbls: whatsInTheBox,db_logins: dataBaseLogins):
        not_found = []
        curnt_tables = curnt_tbls.whats_in_the_box(db_logins)
        for tbls in self.tbl_dicts.keys():
            if tbls not in curnt_tables.keys():
                not_found.append(tbls)
        if len(not_found) > 0:
            print(f"{len(not_found)} {"table was" if len(not_found) == 1 else "tables were"} not found")
            return False
        else:
            return True

    def check_fields(self, curnt_tbls: whatsInTheBox,db_logins: dataBaseLogins):
        fields_not_found = []
        wrong_types = {}
        curnt_tables = curnt_tbls.whats_in_the_box(db_logins)
        for tbl_key in self.tbl_dicts.keys():
            if tbl_key in  curnt_tables.keys():
                for fields, types in self.tbl_dicts[tbl_key].items():
                    if fields not in curnt_tables[tbl_key].keys():
                        fields_not_found.append(fields)
                    else:
                        if types != curnt_tables[tbl_key][fields]:
                            wrong_types[fields] = curnt_tables[tbl_key][fields]
        if len(fields_not_found) > 0 or len(wrong_types) > 0:
            print(f"{len(fields_not_found)} {"field" if len(fields_not_found) == 1 else "fields"} not found")
            print(f"{len(wrong_types)} {"type" if len(wrong_types) == 1 else "types"} are incorrect")
            return False
        else:
            return True

class buildDbJSON:
    """ code to build JSON files that show the required database tables
        - these files are for configuration and to aid processing
        - each table is a seperate JSON file
        - each JSON files shows the field names and types
    """
    def __init__(self, path: str):
        self.data_path = path

    def loadtbls(self, curnt_tbls: whatsInTheBox):
        for key, tbl in curnt_tbls.whats_in_the_box():
            path = (f'{self.data_path}/{key}.JSON')
            print(path)
            with open(path,"w") as jfile:
                json.dump(tbl, jfile,indent=4)

class runSQLscripts:
    def __init__(self, path: str):
        """
            path is path to postgre files
        """
        self.path = path

    def run_script(self, db_logins: dataBaseLogins, script_name: str):
        """
            Runs sql script on db
        """
        script_path = (f"{self.path}/{script_name}")
        with open(script_path, 'r') as script_file:
            sql_drops = script_file.read()
        with psycopg.connect(db_logins.connection_string()) as conn:
            with conn.cursor() as cur:
                cur.execute(sql_drops)

    def reset_db(self, db_logins: dataBaseLogins,):
        """
            Drops all tables then creates all tables and constraints
            then runs fixed data script
        """
        script_list = ['99.drop_all_tables.sql','01_create_tables.sql','02_alter_tables.sql','03 fixed_data.sql']
        for script in script_list:
            self.run_script(db_logins,script)
    
