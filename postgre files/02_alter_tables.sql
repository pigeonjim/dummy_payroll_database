-- Script to add foreigns keys and other constraints

--Add foreign keys
ALTER TABLE office ADD CONSTRAINT office_er_fk FOREIGN KEY (er_id)
    REFERENCES employer (er_id) ON DELETE RESTRICT;

ALTER TABLE ee_jobs ADD CONSTRAINT eejobs_ee_fk FOREIGN KEY (ee_no)
    REFERENCES employee (ee_no) ON DELETE RESTRICT;

ALTER TABLE ee_jobs ADD CONSTRAINT eejobs_office_fk FOREIGN KEY (office_code)
    REFERENCES office (office_code) ON DELETE RESTRICT;

ALTER TABLE payroll_runs ADD CONSTRAINT paruns_er_fk FOREIGN KEY (er_id)
    REFERENCES employer (er_id) ON DELETE RESTRICT;

ALTER TABLE payslips ADD CONSTRAINT pslps_runid_fk FOREIGN KEY (runid)
    REFERENCES payroll_runs (runid) ON DELETE RESTRICT;

ALTER TABLE payslips ADD CONSTRAINT pslps_job_fk FOREIGN KEY (job_id)
    REFERENCES ee_jobs (job_id) ON DELETE RESTRICT;

ALTER TABLE payments ADD CONSTRAINT pmnts_pslps_fk FOREIGN KEY (payslip_id)
    REFERENCES payslips (payslip_id) ON DELETE RESTRICT;

ALTER TABLE payments ADD CONSTRAINT pmnts_payconfig_fk FOREIGN KEY (payment_configid)
    REFERENCES payment_config (payment_configid) ON DELETE RESTRICT;

ALTER TABLE deductions ADD CONSTRAINT ded_pslps_fk FOREIGN KEY (payslip_id)
    REFERENCES payslips (payslip_id) ON DELETE RESTRICT;

ALTER TABLE deductions ADD CONSTRAINT ded_deconfig_fk FOREIGN KEY (deduction_configid)
    REFERENCES deduction_config (deduction_configid) ON DELETE RESTRICT;

-- foreign keys needed due to addtion of frequency table

ALTER TABLE ee_jobs ADD CONSTRAINT eejobs_freq_fk FOREIGN KEY (freq_id)
    REFERENCES frequency (freq_id) ON DELETE RESTRICT;

ALTER TABLE payroll_runs ADD CONSTRAINT pruns_freq_fk FOREIGN KEY (freq_id)
    REFERENCES frequency (freq_id) ON DELETE RESTRICT;

ALTER TABLE payslips ADD CONSTRAINT pslps_freq_fk FOREIGN KEY (freq_id)
    REFERENCES frequency (freq_id) ON DELETE RESTRICT;

-- UNIQUE constraints

ALTER TABLE payroll_runs ADD CONSTRAINT uq_pruns_oneperiod_perer UNIQUE (er_id, freq_id, tax_year, tax_period);
ALTER TABLE payslips ADD CONSTRAINT uq_pslps_ajob_perperiod UNIQUE (job_id,runid);

--- FIX to enforce one payslip, per job, per payrun where the job frequency matches the payslip frequency

    -- UNIQUES for composite foreign keys to use
ALTER TABLE ee_jobs ADD CONSTRAINT uq_eejobs_freq UNIQUE (job_id, freq_id);
ALTER TABLE payroll_runs ADD CONSTRAINT uq_pruns_freq UNIQUE (runid, freq_id);

    -- Foreign keys in payslips into payroll runs
ALTER TABLE payslips ADD CONSTRAINT pslps_job_compfk FOREIGN KEY (job_id, freq_id)
    REFERENCES ee_jobs (job_id, freq_id) ON DELETE RESTRICT;

ALTER TABLE payslips ADD CONSTRAINT pslps_pruns_compfk FOREIGN KEY (runid, freq_id)
    REFERENCES payroll_runs (runid, freq_id) ON DELETE RESTRICT;

-- REGEX checks

ALTER TABLE employee ADD CONSTRAINT regex_ee_pcode CHECK (post_code ~ '^[0-9A-Z]{2,4} [0-9][A-Z]{2}$');

ALTER TABLE employee ADD CONSTRAINT regex_ee_nino CHECK (ni_number ~ '^[A-Z]{2}\d{6}[A-D]$');

ALTER TABLE employer ADD CONSTRAINT regex_er_taxref CHECK (tax_ref ~ '^\d{3}/[A-Z0-9]{6}$');

ALTER TABLE employer ADD CONSTRAINT regex_er_sortcd CHECK (bank_sort_code ~ '^\d{2}-\d{2}-\d{2}$');

ALTER TABLE employer ADD CONSTRAINT regex_er_bankno CHECK (bank_account_no ~ '^\d{8}$');

ALTER TABLE office ADD CONSTRAINT regex_off_pcode CHECK (post_code ~ '^[0-9A-Z]{2,4} [0-9][A-Z]{2}$');
