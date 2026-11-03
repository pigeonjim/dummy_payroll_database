**This is a brief summary of the schema - ERD is in the schema docs folder**

**Table	        Fields	                Type	        Constraints**
employee	    ee_no	                INT	            Primary key		
employee	    first_name	            TEXT			
employee	    last_name	            TEXT			
employee	    dob	                    DATE	        Date must be within last 100 years?
employee	    address	                TEXT			
employee	    post_code	            TEXT	        REGEX (2 to 4), space, (3)  all alphanumeric chars		
employee	    ni_number	            TEXT	        REGEX (2 letters), (6 digits),(1 letter)		
                    
employer	    er_id	                INT	            Primary key		
employer	    er_name	                TEXT			
employer	    tax_ref	                TEXT	        REGEX (3 digits) / (6 alphanumeric chars)		UTR
employer	    bank_sort_code	        TEXT	        REGEX (2 digits)-(2 digits)-(2 digits)		
employer	    bank_account_no	        TEXT	        8 digits – padded with zeros if required		
                    
office	        office_code	            INT	            Primary key		
office	        er_id	                INT	            Foreign Key → employer – RESTRICT		
office	        name	                TEXT			
office	        address	                TEXT			
office	        city	                TEXT			
office	        post_code	            TEXT	        REGEX (2 to 4), space, (3)  all alphanumeric chars		
                    
frequency	    freq_id 	            TEXT	        Primary key		
frequency	    frequency	            TEXT			
frequency	    total_periods	        INT			
                    
ee_jobs	        job_id	                INT	            Primary key		
ee_jobs	        ee_no	                INT	            Foreign Key→ employee – RESTRICT		
ee_jobs	        office_code	            INT	            Foreign Key → office – RESTRICTED		
ee_jobs	        job_title	            TEXT			
ee_jobs	        freq_id 	            TEXT	        Foreign Key → frequency – RESTRICTED		
ee_jobs	        start_date	            DATE		    Date must be within last 100 years?
ee_jobs	        leave_date	            DATE	        Cant be before start date		
                    
payment_config	payment_configid	    INT	            Primary key		
payment_config	taxable	                BOOL			
payment_config	niable	                BOOL			
payment_config	description	            TEXT			
                    
deduction_config  deduction_configid	INT	            Primary key		
deduction_config  pre_tax	            BOOL			
deduction_config  pre_ni	            BOOL			
deduction_config  description	        TEXT			
                    
payroll_runs	runid	                INT	            Primary key		only one payroll run per employer, per frequency, per pay period
payroll_runs	er_id	                INT	            Foreign Key → employer – RESTRICT		UNIQUE (er_id, frequency, tax_year, tax_period)
payroll_runs	freq_id 	            TEXT	        Foreign Key → frequency – RESTRICTED		
payroll_runs	tax_year	            INT			
payroll_runs	tax_period	            INT	            1-12 for monthly, 1 to 52 for weekly, 1 to 26 for fortnightly , 1 to 14 for four weekly
                                                        , 1 to 4 for quarterly, 1 for annual		
payroll_runs	pay_date	            DATE			
                    
payslips	    payslip_id	            INT	            Primary key		Only one payrun, per job_id, per payrun UNIQUE(job_id,runid)
payslips	    runid	                INT	            Foreign Key → payroll_runs – RESTRICT		
payslips	    job_id	                INT	            Foreign Key → ee_jobs – RESTRICTED		
payslips        freq_id 	            TEXT	        Foreign Key → frequency – RESTRICTED		
payslips	    tax	                    NUMERIC(8,2)			
payslips	    ee_ni	                NUMERIC(8,2)			
payslips	    er_ni	                NUMERIC(8,2)			
payslips	    ee_pension	            NUMERIC(8,2)			
payslips	    er_pension	            NUMERIC(8,2)			
payslips	    net	                    NUMERIC(8,2)	Stored calculation		
payslips	    gross_taxable_only	    NUMERIC(8,2)	Stored calculation		--taxable but not niable
payslips	    gross_niable_only	    NUMERIC(8,2)	Stored calculation		- niable but not taxable
payslips	    gross_taxable_niable    NUMERIC(8,2)	Stored calculation		
payslips	    gross_notax_noni	    NUMERIC(8,2)	Stored calculation		-- not taxable or niable
payslips	    ded_pretax_preni	    NUMERIC(8,2)	Stored calculation		
payslips	    ded_pretax_only	        NUMERIC(8,2)	Stored calculation		-- pre tax, post ni deduction
payslips	    ded_preni_only	        NUMERIC(8,2)	Stored calculation		-- pre ni, post tax deduction
payslips	    ded_posttax_postni	    NUMERIC(8,2)	Stored calculation		
                    
payments	    payment_ref	            INT	            Primary key		
payments	    payslip_id	            INT	            Foreign Key → payslips – RESTRICT		
payments	    payment_configid	    INT	            Foreign Key → payment_config – RESTRICT		
payments	    amount	                NUMERIC(8,2)			
                    
deductions	    deduction_ref	        INT	            Primary key		
deductions	    payslip_id	            INT	            Foreign Key → payslips – RESTRICT		
deductions	    deduction_configid	    INT	            Foreign Key → deduction_config – RESTRICT		
deductions	    amount	                NUMERIC(8,2)			
