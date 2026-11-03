#this isnt a day to day dairy. It is a place to document milestones, significant problems and other more imortant learnings

03-11-2026
I need to add a field to the ee_job table because a limitaiton of my design. By design an ee can have more than one job and those can be with different ers. Using contraints i can enforce the rule that a job can only be paid once per payrun. However, that does not take into acount frequency. Payroll runs with different frequencies can overlap.
The limitation here is that i cant enforce a simple contraint that prevents this due to the fields required beind held on different tables. A payroll engine would be able handle his (the HMRC have rules about this, including what to do when an ee changes frequency) but I am not coding any processing.
I am also going to add a frequency table to give each frquency the same ID in the tables that use it. I am also going to read more about contraints and see if there is a way to prevent the period overlap mentioned above.
03-11-2026
I have potential solution to preventing a job being paid for more than one frequency in the same time frame. But (a big but) I need to apply it and test it. The proposal is to add frequency to the payslips table then use composite keys to enforce
    one payslip, per job, per payrun where the job frequency matches the payslip frequency.