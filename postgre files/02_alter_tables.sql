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

ALTER TABLE deductions ADD CONSTRAINT ded_decondig_fk FOREIGN KEY (deduction_configid)
    REFERENCES deduction_config (deduction_configid) ON DELETE RESTRICT;
