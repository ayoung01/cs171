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
    a = JSONConverter()

    a[1][2][3] = 4
    a[1][3][3] = 5
    a[1][2]['test'] = 6


    fcsv = open('country.csv', 'rb')
    fjson = open('country.json', 'wb')
    
    # holds the 
    arr = JSONConverter()
    headers = []
    
    line = fcsv.readline()
    lines = line.split('\r\n')
    # print lines
    headers = lines[0].split(',')
    # print headers
    
    lines.pop(0)

    for line in iter(lambda: fcsv.readline(), ""):
    # for line in lines:
        # print line
        row = line.split(',')
        year = row[0].strip()
        if (not year):
            print "AHA!: " + str(x)
            print line
        code = row[2].strip()
        name = row[3].strip()

        temp_dict = {}
        for x in range (4, len(headers)):
            # for each IJAN, ..., IYR, EJAN, ..., EYR
            header = headers[x].strip()
            # first letter of the header (I, E, or B) reveals import, export, or balance
            trade_type = header[:1]

            # rest of header is the month (may contain 'YR')
            month = header[1:]
            # print "trade type: " + trade_type
            # print "month: " + month

            # {year: {month: {code: {imports: #, exports: #, balance:#}}}}
            if code != "none":
                arr[year][month][code][trade_type] = float(row[x])
            else:
                arr[year][month][name][trade_type] = float(row[x])

        # arr[row[0]] = temp_dict
        
    out = json.dumps(arr)
    fjson.write(out)
    fcsv.close()
    fjson.close()

country()