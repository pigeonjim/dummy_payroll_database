# dummy_payroll_database
Project objectives-

To build a database from scratch myself using postgreSQL
To create dummy data using pandas and populate the postgre database
To provide SQL script files and py files that can be easily modified to create small databases of fake data
The database is populated with a very simplified set of payroll data. There is no payroll processing just storage.

Why-

To learn and practice postgreSQL including DDL and DML.
To practice using python and pandas to create fake data and manipulate data as well as connect to a SQL database and populate the tables
The database and code files themselves will be useful for learning purposes and for future projects

Description of the the database-

A summary of the schema and an ERD are included in the schema project folder

Assumptions and simplifications-

There a lot of these because real life payroll is complex and because this is just storage. These include:
Pensions are assumed to be for all EEs, on all payments.
Pensions are assumed to be pre tax, post ni (net pay arrangement)
Tax relief on pensions in real life is complex and depends on tax bandings, this is is ignored. For all EEs taxable gross is reduced by pension, net pay is minus pension.
