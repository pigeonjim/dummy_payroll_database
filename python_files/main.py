import payruns as prs, csv, frequency_data as exd,db_functions, os
from abc import ABC, abstractmethod


def main_app():
    db_logins = db_functions.dataBaseLogins()
    curnt_schma = db_functions.whatsInTheBox()
    tbl_chk_ob = db_functions.checkDbTables('./db_JSON_files')    
    if not tbl_chk_ob.check_tables(curnt_schma,db_logins):
        print("do you want to reset the tables?")
    elif not tbl_chk_ob.check_fields(curnt_schma,db_logins):
        print("Fields are not correct do you want to reset the tables?")
    else:
        print("All tables are correct")

db_logins = db_functions.dataBaseLogins()
scripts = db_functions.runSQLscripts('./postgre_files')
scripts.reset_db(db_logins)
#main_app()
#main application
# 0 Check DB exists
    #0.1 get DB name, user and password
    #0.2 check tables exist
    #0.3 build missing tables
#1.0 frequencies
    #1.1 already in tables
        #1.1.1 read into dictionary
    #1.2 input by csv or end user input
#2.0 create payruns
#3.0 payments config
#4.0 deductions config
