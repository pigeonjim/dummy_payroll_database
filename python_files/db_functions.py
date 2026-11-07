import psycopg,  getpass

class dataBaseLogins:
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
            if choice == 'Y':
                self.get_logins()

    def __str__(self):
        return (f"Current database dbname = {self.__db_name} and username = {self.__user}")