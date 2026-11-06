import payruns as prs, csv, frequency_data as exd
from abc import ABC, abstractmethod

def get_no_ees():
    while True:
        try:
            ee_no = int(input("How many employees would you like data for? Maximum is 1000 -"))
            if ee_no < 1 or ee_no >  1000:
                raise ValueError
        except ValueError:
            print("Number of employees should be a number more than 0 and less than 1001")
    return ee_no

def generate_data():

    print("This application will generate fake payroll data for the database and INSERT the data into the database")
    number_ees = get_no_ees()
    print()
    fd= exd.keyFreqData()
    print(fd.get_freq_data())



#main application
#1.0 frequencies
    #1.1 already in tables
        #1.1.1 read into dictionary
    #1.2 input by csv or end user input
#2.0 create payruns

#3.0 payments config
#4.0 deductions config
