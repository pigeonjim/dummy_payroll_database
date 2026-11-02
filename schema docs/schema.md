**This is a brief summary of the schema without foreign keys or constraints**

Tbl: **employee**
Fields:
ee_no (primary key), first_name, last_name, dob, address, post_code, ni_number

Tbl: **employer**
Fields:
er_id (primary key), er_name, tax_ref, bank_sort_code, bank_account_no

Tbl: **office**
Fields:
office_code (primary key), name, er_id, address, city, post_code

Tbl: **ee_jobs**
Fields:
job_id  (primary key), ee_no, office_code, job_title, start_date, leave_date

Tbl: **payment_config**
Fields:
payment_configid (primary key), taxable, niable, description

Tbl **deduction_config**
Fields:
deduction_configid (primary key), pre_tax, pre_ni, description

Tbl: **payroll_runs**
Fields:
runid (primary key), er_id,frequency, tax_year, tax_period, pay_date

Tbl: **payslips**
Fields:
payslip_id (primary key), runid, job_id, tax, ee_ni, er_ni, ee_pension, er_pension
Stored/calculated totals: net, gross_taxbale_niable, gross_taxable_only, gross_niable_only, gross_no_tax_ni
                          , ded_pretax_preni, ded_pretax_only, ded_preni_only, ded_posttax_postni

Tbl: **payments**
Fields:
payments_ref (primary key), payslip_id, payment_configid, amount

Tbl **deductions**
Fields:
deduction_ref (primary key), payslip_id, deduction_configid, amount