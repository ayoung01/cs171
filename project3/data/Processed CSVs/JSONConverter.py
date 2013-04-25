'''
Created on Mar 15, 2013

@author: ayoung
'''
import json

class JSONConverter(dict):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value

def country():
    fcsv = open('country.csv', 'rb')
    fjson = open('country.json', 'wb')
    
    result = JSONConverter()
    headers = []
    
    line = fcsv.readline()
    lines = line.split('\r\n')
    headers = lines[0].split(',')
    
    lines.pop(0)

    for line in iter(lambda: fcsv.readline(), ""):
        row = line.split(',')
        year = row[0].strip()
        code = row[2].strip()
        name = row[3].strip()

        for x in range (4, len(headers)):
            # for each IJAN, ..., IYR, EJAN, ..., EYR
            header = headers[x].strip()
            # first letter of the header (I, E, or B) reveals import, export, or balance
            trade_type = header[:1]

            # rest of header is the month (may contain 'YR')
            month = header[1:]

            # {year: {month: {code: {imports: #, exports: #, balance:#}}}}
            if code != "none":
                result[year][month][code][trade_type] = float(row[x])
            else:
                result[year][month][name][trade_type] = float(row[x])

    out = json.dumps(result)
    fjson.write(out)
    fcsv.close()
    fjson.close()

def by_use():
    fcsv = open('by_use.csv', 'rb')
    fjson = open('by_use.json', 'wb')
    
    result = JSONConverter()
    headers = []
    year = ""
    
    line = fcsv.readline()
    lines = line.split('\r\n')
    headers = lines[0].split(',')
    
    lines.pop(0)

    for line in iter(lambda: fcsv.readline(), ""):
        row = line.split(',')
        for x in range(1, len(headers)):
            # for each IJAN, ..., IYR, EJAN, ..., EYR
            header = headers[x].strip()
            # first letter of the header (I, E, or B) reveals import, export, or balance
            trade_type = header[:1]
            # rest of header is the use
            use = header[1:]

            # if we encounter a row that is a year, set current year
            if (row[0][:1] == "1") or (row[0][:1] == "2"):
                year = row[0]
                try:
                    result[year]["total_year"][trade_type][use] = float(row[x])
                except:
                    result[year]["total_year"][trade_type][use] = "none"
            # else we are record the month's data
            else:
                month = row[0]
                # {year: {month: {I: {total: #, foods: #, ...} E: {...}}}}
                try:
                    result[year][month][trade_type][use] = float(row[x])
                except:
                    result[year][month][trade_type][use] = "none"
    out = json.dumps(result)
    fjson.write(out)
    fcsv.close()
    fjson.close()

# country()
by_use()