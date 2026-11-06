-- code for tables where data will not be loaded in from python or /code

--frequency table
INSERT INTO frequency (freq_id, frequency, total_periods) VALUES ('M','Monthly',12);
INSERT INTO frequency (freq_id, frequency, total_periods) VALUES ('W','Weekyl',52);
INSERT INTO frequency (freq_id, frequency, total_periods) VALUES ('F','Fortnightly',26);
INSERT INTO frequency (freq_id, frequency, total_periods) VALUES ('FW','Four_weekly',13);
INSERT INTO frequency (freq_id, frequency, total_periods) VALUES ('Q','Quarterly',4);
INSERT INTO frequency (freq_id, frequency, total_periods) VALUES ('A','Annual',1);

--payments config
INSERT INTO payment_config (payment_configid, taxable, niable, description) VALUES ('P1','1','1','Salary');
INSERT INTO payment_config (payment_configid, taxable, niable, description) VALUES ('P2','1','1','Overtime');
INSERT INTO payment_config (payment_configid, taxable, niable, description) VALUES ('P3','1','1','Hourly');
INSERT INTO payment_config (payment_configid, taxable, niable, description) VALUES ('P4','0','0','Expenses');
INSERT INTO payment_config (payment_configid, taxable, niable, description) VALUES ('P5','1','0','BIK');
INSERT INTO payment_config (payment_configid, taxable, niable, description) VALUES ('P6','1','1','Bonus');
INSERT INTO payment_config (payment_configid, taxable, niable, description) VALUES ('P7','0','0','Petty_cash');
INSERT INTO payment_config (payment_configid, taxable, niable, description) VALUES ('P8','1','1','Holiday');
INSERT INTO payment_config (payment_configid, taxable, niable, description) VALUES ('P9','0','0','Fuel');
INSERT INTO payment_config (payment_configid, taxable, niable, description) VALUES ('P10','1','1','Overnight');

--deductions config
INSERT INTO deduction_config (deduction_configid, pre_tax, pre_ni, description) VALUES ('D1','0','0','Loan');
INSERT INTO deduction_config (deduction_configid, pre_tax, pre_ni, description) VALUES ('D2','0','0','Parking');
INSERT INTO deduction_config (deduction_configid, pre_tax, pre_ni, description) VALUES ('D3','1','0','BIK_Ded');
INSERT INTO deduction_config (deduction_configid, pre_tax, pre_ni, description) VALUES ('D4','1','1','Overpayment');
INSERT INTO deduction_config (deduction_configid, pre_tax, pre_ni, description) VALUES ('D5','1','1','Sickleave');
INSERT INTO deduction_config (deduction_configid, pre_tax, pre_ni, description) VALUES ('D6','1','1','Cycle_to_work');
INSERT INTO deduction_config (deduction_configid, pre_tax, pre_ni, description) VALUES ('D7','0','0','Gym');