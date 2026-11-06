from abc import ABC, abstractmethod
import csv

class readFreqDataInterface(ABC):
    """interface for getting frequency data input and processing into a dictionary
        Key is string representation of frquency and value is number of periods per frequency"""
    @abstractmethod
    def get_freq_data(self):
        """read in frequency data
        process frequency data and output dict
        Key is string representation of frquency and value is number of periods per frequency"""

    @property
    @abstractmethod
    def freq_data(self) -> dict[str,int]:
        """The getter for the dictionary"""

class readFreqDataCSV(readFreqDataInterface):
    """Get frequency data from CSV import and process into frequency dictionary"""
    def __init__(self, path: str):
        self.__path = path
        self.get_freq_data()

    def get_freq_data(self):
        self.__freq_data = {} 
        with open(self.__path, newline='') as freq_file:
            self.__reader_ob = csv.reader(freq_file)
            next(self.__reader_ob) #to skip header row       
            for row in self.__reader_ob:
                try:
                    self.__freq_data[row[0]] = int(row[2])
                except ValueError:
                    print("Row error")
                    continue

    @property 
    def freq_data(self):
        return self.__freq_data