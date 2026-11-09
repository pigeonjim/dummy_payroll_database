# dummy_payroll_database
PostgreSQL and Python with pandas and psycopg

Project objectives-

To build a database from scratch myself using postgreSQL
To create dummy data and populate the postgre database
To provide SQL script files and py files that can be easily modified to create small databases of fake data
The database is populated with a very simplified set of payroll data. There is no payroll processing just storage.

Why-

To learn and practice postgreSQL including DDL and DML.
To practice using python and pandas to create fake data and manipulate data as well as connect to a SQL database and populate the tables
The database and code files themselves will be useful for learning purposes and for future projects

Description of the the database-

A summary of the schema and an ERD are included in the schema project folder

Notes on how, why and assumptions-

This program can not create a new database. You will need to create a blank data base youeself.
If you need help to install PostgreSQL and configure it refer the office guide or use a search engine to look for "Getting Started with PostgreSQL"

When you start the program you will be  askd for the database name, user name and password (this will not be displayed in the console). The connection will then be tested.
The database will be queried to see if all the required tables and fields with the correct type are present. 

    Main options

    - Drop all tables to reset to a blank database
    - Create all tables, fields and constraints
    - Generate data and populate database


    Generator notes -
There are a lot of assumptions because real life payroll is complex and this is just storage.

Pensions are assumed to be for all EEs, on all payments.
Pensions are assumed to be pre tax, post ni (net pay arrangement)
Tax relief on pensions in real life is complex and depends on tax bandings, this is is ignored. For all EEs taxable gross is reduced by pension.

NI numbers have a more complex set of rules that those enfored by generator's REGEX and the SQL constraint

Tax is simplified - No tax below 20k, 20% from 20k up to 40k and 40% above 40k
NI is simplified - EE 8% from 12k up to 48k then 2%
                 - ER from 12k 15%

EE age check is done in the data generator so there is no constraint on the db field

Tax years are written as a year but in reality this would be the start year for example 2026 would mean 26/27 or 06/04/26-05/04/27



-- If you dont want to use the generator there is a set of fake data in CSV files that you can \copy into your database. These are located in the folder called
    Sample data to import. The data for frequency, payment_config and deduction_config are also in there in CSV.