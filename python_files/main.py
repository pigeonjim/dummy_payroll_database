import csv, input_data as exd, db_functions, os
from abc import ABC, abstractmethod

def db_checking(db_logins: db_functions.dataBaseLogins):
    """
        Checks all tables, fields and types currently in the database
        If anything is incorrect there is an option to reset the DB
        If db schema is correct after checking or by reset returns True
        Else returns False
    """
    while True:
        curnt_schma = db_functions.whatsInTheBox()
        tbl_chk_ob = db_functions.checkDbTables('./db_JSON_files')  
        scripts = db_functions.runSQLscripts('./postgre_files')  
        if not tbl_chk_ob.check_tables(curnt_schma,db_logins):
            if input("do you want to reset the tables Y or N?").upper() == 'Y':
                scripts.reset_db(db_logins)
                return True
            else:
                return False
        elif not tbl_chk_ob.check_fields(curnt_schma,db_logins):
            if input("Fields are not correct do you want to reset the tables?").upper() == 'Y':
                scripts.reset_db(db_logins)
                return True
            else:
                return False
        else:
            print("All tables are correct")
            return True

def main_app():
    db_logins = db_functions.dataBaseLogins()
    while True:
        if not db_checking(db_logins):
            break

main_app()
#main application
# 0 Check DB exists
    #0.1 get DB name, user and password
    #0.2 check tables exist
    #0.3 build missing tables
#1.0 
    #1.1 Frquency, pay_config and ded_config
        #1.1.1 Do they need populated?
        #1.1.2 option to add to tables via interface
#2.0 Create data for DB
