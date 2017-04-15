import csv
import os

class BadData(Exception):
    def __init__(self):
        raise NotImplementedError

class AbstractRecord:
    name = []
    def __init__(self):
        raise(NotImplementedError)

class BaseballStatRecord(AbstractRecord):
    def __init__(self, fileName):
        pass


    def __str__(self):
        return '{}({})'.format(recordType, self.nameString)
class StockStatRecord(AbstractRecord):
    def __init__(self):
        company_name = []
        exchange_country = []
        price = []
        exchange_rate = []
        shares_outstanding = []
        net_income = []

    def __str__(self, recordType):
        return '{}({})'.format(recordType, self.nameString)



class Record(AbstractRecord):
    company_name = []
    exchange_country = []
    price = []
    exchange_rate = []
    shares_outstanding = []
    net_income = []
    nameString = ''
    def __init__(self, fileName):
        market_value_usd = []
        pe_ratio = []
        salary = []
        G = []
        AVG = []
        with open(fileName, 'r') as openFile:
            f_csv = csv.reader(openFile)
            for row in f_csv:
                #continue
                #if(fileName == "")
                self.name.append(row[0])
                self.exchange_country.append(row[1])
                self.company_name.append(row[2])
                self.price.append(row[3])
                self.exchange_rate.append(row[4])
                self.shares_outstanding.append(row[5])
                self.net_income.append(row[6])
            openFile.close()
        print(self.name)
        self.nameString = ",".join(self.name)
        print(self.nameString)
        self.nameString = self.nameString.strip(self.name[0] + ",")
        print(self.nameString)
        #self.exchange_countryString = ",".join(self.exchange_country)

    def __str__(self):
        return '{}({})'.format(self.nameString[0], self.nameString)


class AbstractCSVReader:
    def __init__(self, fileName):
        self.fileName = fileName

    def row_to_record(self, row):
        self.row = row
        raise BadData

    def load(self):
        readList = []
        with open(self.fileName, r) as openFile:
            f_csv = csv.reader(openFile)
            for row in f_csv:
                try:
                    self.row_to_record(row)
                except BadData:
                    continue
                else:
                    readList = readList.append(row)
            openFile.close()
        return readList

class BaseballCSVReader(AbstractCSVReader):
    def __init__(self):
        super().__init__()
    def row_to_record(self, row):
        tmpTuple = ()
        pass



class StocksCSVReader(AbstractCSVReader):
    pass





if __name__ == '__main__':



a = Record("StockValuations.csv")
print(a.__str__())



