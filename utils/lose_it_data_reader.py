import csv
from datetime import datetime

class LoseItEntry(object):
    def __init__(self, name, calories_str, date_str):
        self.name = name
        self.calories = int(float(calories_str))
        self.date = datetime.strptime(date_str, '%m/%d/%Y').date()
    
    def __repr__(self):
        return "<LoseItEntry('%s','%d','%s')>" % (self.name, self.calories, self.date)

class LoseItDataReader(object):
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.csv_reader = csv.reader(self.csv_file, delimiter=',', quotechar='"')
        self.headers = self.csv_reader.next()
        self.name_index = self._find_index('Name')
        self.calories_index = self._find_index('Calories')
        self.date_index = self._find_index('Date')
    
    def __iter__(self):
        return self
    
    def next(self):
        row_data = self.csv_reader.next()
        
        name = ''
        if not self.name_index is None:
            name = row_data[self.name_index]
            
        calories = 0
        if not self.calories_index is None:
            calories = row_data[self.calories_index]
            
        date_str = None
        if not self.date_index is None:
            date_str = row_data[self.date_index]
            
        return LoseItEntry(name, calories, date_str)
    
    def _find_index(self, column_header):
        try:
            return self.headers.index(column_header)
        except ValueError:
            return None