import payruns as prs, csv, extract_data as exd
from abc import ABC, abstractmethod




#def getFreqData(freq_data: readFreqDataInterface):
   # print(freq_data.freq_data)


fd= exd.readFreqDataCSV('./Sample_data/frequency_table.csv')
print(fd.freq_data)




#pr = prs.Payruns()
#print(pr.current_taxyear)
