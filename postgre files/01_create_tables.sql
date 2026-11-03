-- Create all tables with primary keys
-- No constraints. These will be coded in an ALTER TABLE file

CREATE TABLE employee(
    ee_no INT  PRIMARY KEY
    , first_name TEXT
    , last_name TEXT
    , dob DATE
    , address TEXT
    , post_code TEXT
    , ni_number TEXT
    );

CREATE TABLE employer(
    er_id INT PRIMARY KEY
    , er_name TEXT
    , tax_ref TEXT
    , bank_sort_code TEXT
    , bank_account_no TEXT
    );

CREATE TABLE office(
    office_code INT PRIMARY KEY
    , er_id INT
    , name  TEXT
    , address TEXT
    , city TEXT
    , post_code TEXT
    );

CREATE TABLE frequency(
    freq_id TEXT PRIMARY KEY
    , frequency TEXT
    , total_periods INT
    )

CREATE TABLE ee_jobs(
    job_id INT PRIMARY KEY
    , ee_no INT
    , office_code INT
    , job_title TEXT
    , freq_id TEXT
    , start_date DATE
    , leave_date DATE
    );

CREATE TABLE payment_config(
    payment_configid INT PRIMARY KEY
    , taxable BOOl
    , niable BOOl
    , description TEXT
    );

CREATE TABLE deduction_config(
    deduction_configid INT PRIMARY KEY
    , pre_tax BOOl
    , pre_ni BOOl
    , description TEXT
    );

CREATE TABLE payroll_runs(
    runid INT PRIMARY KEY
    , er_id INT
    , freq_id TEXT
    , tax_year INT
    , tax_period INT
    , pay_date DATE
    );

CREATE TABLE payslips(
    payslip_id INT PRIMARY KEY
    , runid INT
    , job_id INT
    , freq_id TEXT
    , tax NUMERIC(8,2)
    , ee_ni NUMERIC(8,2)
    , er_ni NUMERIC(8,2)
    , ee_pension NUMERIC(8,2)
    , er_pension NUMERIC(8,2)
    , net NUMERIC(8,2)
    , gross_taxable_only NUMERIC(8,2) --taxable but not niable
    , gross_niable_only NUMERIC(8,2) -- niable but not taxable
    , gross_taxable_niable NUMERIC(8,2)
    , gross_notax_noni NUMERIC(8,2) -- not taxable or niable
    , ded_pretax_preni NUMERIC(8,2)
    , ded_pretax_only NUMERIC(8,2) -- pre tax, post ni deduction
    , ded_preni_only NUMERIC(8,2) -- pre ni, post tax deduction
    , ded_posttax_postni NUMERIC(8,2) 
    );

CREATE TABLE payments(
    payment_ref INT PRIMARY KEY
    , payslip_id INT
    , payment_configid INT
    , amount NUMERIC(8,2)
    );

CREATE TABLE deductions(
    deduction_ref INT PRIMARY KEY
    , payslip_id INT
    , deduction_configid INT
    , amount NUMERIC(8,2)
    );