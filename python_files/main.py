import payruns as prs, csv, frequency_data as exd,db_functions
from abc import ABC, abstractmethod


def main_app():
    db_logins = db_functions.dataBaseLogins()
    chk_tbls = db_functions.checkDbTables()
    #chk_tbls.get_current_tbls(db_logins)
    bjs = db_functions.buildDbJSON()
    bjs.loadtbls(db_logins)


main_app()
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
