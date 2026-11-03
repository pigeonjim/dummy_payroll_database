-- Create all tables with primary keys
-- No constraints. These will be coded in an ALTER TABLE file

CREATE TABLE employee(
    ee_no INT  PRIMARY KEY
    , first_name TEXT NOT NULL
    , last_name TEXT NOT NULL
    , dob DATE
    , address TEXT
    , post_code TEXT
    , ni_number TEXT NOT NULL
    );

CREATE TABLE employer(
    er_id INT PRIMARY KEY
    , er_name TEXT NOT NULL
    , tax_ref TEXT NOT NULL
    , bank_sort_code TEXT
    , bank_account_no TEXT
    );

CREATE TABLE office(
    office_code INT PRIMARY KEY
    , er_id INT NOT NULL
    , name  TEXT NOT NULL
    , address TEXT
    , city TEXT
    , post_code TEXT
    );

CREATE TABLE frequency(
    freq_id TEXT PRIMARY KEY
    , frequency TEXT UNIQUE NOT NULL
    , total_periods INT
    );

CREATE TABLE ee_jobs(
    job_id INT PRIMARY KEY
    , ee_no INT NOT NULL
    , office_code INT NOT NULL
    , job_title TEXT NOT NULL
    , freq_id TEXT NOT NULL
    , start_date DATE NOT NULL
    , leave_date DATE
    );

CREATE TABLE payment_config(
    payment_configid INT PRIMARY KEY
    , taxable BOOl NOT NULL
    , niable BOOl NOT NULL
    , description TEXT NOT NULL
    );

CREATE TABLE deduction_config(
    deduction_configid INT PRIMARY KEY
    , pre_tax BOOl NOT NULL
    , pre_ni BOOl NOT NULL
    , description TEXT NOT NULL
    );

CREATE TABLE payroll_runs(
    runid INT PRIMARY KEY
    , er_id INT NOT NULL
    , freq_id TEXT NOT NULL
    , tax_year INT NOT NULL
    , tax_period INT NOT NULL
    , pay_date DATE NOT NULL
    );

CREATE TABLE payslips(
    payslip_id INT PRIMARY KEY
    , runid INT NOT NULL
    , job_id INT NOT NULL
    , freq_id TEXT NOT NULL
    , tax NUMERIC(8,2) NOT NULL DEFAULT 0
    , ee_ni NUMERIC(8,2) NOT NULL DEFAULT 0
    , er_ni NUMERIC(8,2) NOT NULL DEFAULT 0
    , ee_pension NUMERIC(8,2) NOT NULL DEFAULT 0
    , er_pension NUMERIC(8,2) NOT NULL DEFAULT 0
    , net NUMERIC(8,2) NOT NULL DEFAULT 0
    , gross_taxable_only NUMERIC(8,2) NOT NULL DEFAULT 0  --taxable but not niable
    , gross_niable_only NUMERIC(8,2) NOT NULL DEFAULT 0 -- niable but not taxable
    , gross_taxable_niable NUMERIC(8,2) NOT NULL DEFAULT 0
    , gross_notax_noni NUMERIC(8,2) NOT NULL DEFAULT 0 -- not taxable or niable
    , ded_pretax_preni NUMERIC(8,2) NOT NULL DEFAULT 0
    , ded_pretax_only NUMERIC(8,2) NOT NULL DEFAULT 0 -- pre tax, post ni deduction
    , ded_preni_only NUMERIC(8,2) NOT NULL DEFAULT 0 -- pre ni, post tax deduction
    , ded_posttax_postni NUMERIC(8,2) NOT NULL DEFAULT 0 
    );

CREATE TABLE payments(
    payment_ref INT PRIMARY KEY
    , payslip_id INT NOT NULL
    , payment_configid INT NOT NULL
    , amount NUMERIC(8,2) NOT NULL DEFAULT 0
    );

CREATE TABLE deductions(
    deduction_ref INT PRIMARY KEY
    , payslip_id INT NOT NULL
    , deduction_configid INT NOT NULL
    , amount NUMERIC(8,2) NOT NULL DEFAULT 0 NOT NULL DEFAULT 0
    );