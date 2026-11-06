import datetime, csv, frequency_data as exd


class payrollYear:
    def  __init__(self,tax_year: int):
        self.__start = datetime.datetime(tax_year,4,5)

class Payruns:
    def __init__(self):
        self.__check_current_year()
        self.frequencies = {'M': 12, 'W': 52, 'F': 26}

    def __check_current_year(self):
        while True:
            try:
                what_year = int(input("Please input current tax year: "))
                if what_year < 2000 or what_year > 2100:
                    print("Current Tax year must be between 2000 and 2100")
                else:
                    self.__current_taxyear = datetime.datetime(what_year,4,5)
                    break
            except ValueError:
                print("Year must be a number")

    def get_frequencies(self, freq_data: exd.readFreqDataInterface):
        self.frequencies = freq_data.get_freq_data()
        


    @property
    def current_taxyear(self):
        return self.__current_taxyear

class payrunsApplication:
    """application to create 10 years of payroll runs
        for all frequencies.
        Current year plus 4 previous and 5 in the future"""
    def __init__(self):
        self.__payruns = Payruns