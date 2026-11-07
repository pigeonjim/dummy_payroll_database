"""
This module has the functionality for the frequency table in the database
It has an interface to allow for different input methods
and a controller class frequencyData

readFreqDataInterface
    The following functions use the interface
    and return a dictionary where
        Key = freq_id : Value = No of periods;
    readFreqDataCSV - Imports data from csv
    keyFreqData - Allows for data entry via the console
    qryFreqDataSQL - Will query the frequency table

updateTbl - INSERTS and UPDATES the frequency table

"""


from abc import ABC, abstractmethod
import psycopg ,csv

class readFreqDataInterface(ABC):
    """interface for getting frequency data input and processing into a dictionary
        Key is string representation of frquency and value is number of periods per frequency"""
    @abstractmethod
    def get_freq_data(self):
        """read in frequency data
        process frequency data and output dict
        Key is string representation of frquency and value is number of periods per frequency"""

class readFreqDataCSV(readFreqDataInterface):
    """Get frequency data from CSV import and process into frequency dictionary"""
    def __init__(self, path: str):
        self.__path = path

    def get_freq_data(self):
        freq_data = {} 
        with open(self.__path, newline='') as freq_file:
            self.__reader_ob = csv.reader(freq_file)
            next(self.__reader_ob) #to skip header row       
            for row in self.__reader_ob:
                try:
                    freq_data[row[0]] = int(row[2])
                except ValueError:
                    print("Row error")
                    continue
        return freq_data

class keyFreqData(readFreqDataInterface):
    def __init__(self):
        self._freq_data = {}

    def get_freq_data(self):
        print("Input the required frequencies in the format code then number")
        print("For example: ")
        print("When asked for the code input 'M' for monthly")
        print("When asked for the number of periods input 12 for monthly")
        print("Enter 'quit' at the code prompt to quit and save")
        while True:
            fcode = input("please input the frequency code: ")
            if fcode == "quit":
                break
            try:
                periods = int(input(f"please input the number of periods for frequency {fcode}: "))
                if periods > 52 or periods < 1:
                    raise ValueError
                self._freq_data[fcode] = [periods]
            except ValueError:
                print(f"Number of periods must be an integer value above 0 and at most 52")
        if len(self._freq_data) < 1:
            return None
        else:
            return self._freq_data

class qryFreqDataSQL(readFreqDataInterface):
    def __init__(self, db_ob):
        pass



class frequencyData:
    def __init__(self):
        pass

    def which_input(self):
        #check tables?
        in_tables = input("Is the frequency table already populated?")