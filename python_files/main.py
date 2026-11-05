import payruns as prs, csv

freq_data = {}
with open('../Sample_data/frequency_table.csv', newline='') as freq_file:
    fr_reader = csv.reader(freq_file)
    next(fr_reader) #to skip header row
    for row in fr_reader:
        try:
            freq_data[row[0]] = int(row[2])
        except ValueError:
            print("Row error")
            continue
print(freq_data)



#pr = prs.Payruns()
#print(pr.current_taxyear)