'''
Created on Mar 15, 2013

@author: ayoung
'''
import json

class JSONConverter(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
def data():
    fcsv = open('data.csv', 'rb')
    fjson = open('data.json', 'wb')
    
    arr = {}
    headers = []
    
    line = fcsv.readline()
    lines = line.split('\r')
    headers = lines[0].split(',')
    #print headers
    lines.pop(0)
    
    net_oda = {}
    oda_ldc = {}
    oda_lic = {}
    oda_lmic = {}
    oda_umic = {}
    s_sahara = {}
    s_asia = {}
    oceania = {}
    n_africa = {}
    europe = {}
    latin_am = {}
    soc_infra = {}
    econ_infra = {}
    production  = {}
    multisector = {}
    hum_aid = {}
    admin_expenses = {}
    other = {}
    
    #for line in iter(lambda: fcsv.readline(), ""):
    for line in lines:
    #    print line    
        arr1 = line.split(',')
        print arr1
        net_oda[arr1[0]] = float(arr1[1])
        oda_ldc[arr1[0]] = float(arr1[2])
        oda_lic[arr1[0]] = float(arr1[3])
        oda_lmic[arr1[0]] = float(arr1[4])
        oda_umic[arr1[0]] = float(arr1[5])
        s_sahara[arr1[0]] = float(arr1[6])
        s_asia[arr1[0]] = float(arr1[7])
        oceania[arr1[0]] = float(arr1[8])
        n_africa[arr1[0]] = float(arr1[9])
        europe[arr1[0]] = float(arr1[10])
        latin_am[arr1[0]] = float(arr1[11])
        soc_infra[arr1[0]] = float(arr1[12])
        econ_infra[arr1[0]] = float(arr1[13])
        production[arr1[0]] = float(arr1[14])
        multisector[arr1[0]] = float(arr1[15])
        hum_aid[arr1[0]] = float(arr1[16])
        admin_expenses[arr1[0]] = float(arr1[17])
        other[arr1[0]] = float(arr1[18])
    
    arr["net_oda"] = net_oda
    arr["oda_ldc"] = oda_ldc
    arr["oda_lic"] = oda_lic
    arr["oda_lmic"] = oda_lmic
    arr["oda_umic"] = oda_umic
    arr["s_sahara"] = s_sahara
    arr["s_asia"] = s_asia
    arr["oceania"] = oceania
    arr["n_africa"] = n_africa
    arr["europe"] = europe
    arr["latin_am"] = latin_am
    arr["soc_infra"] = soc_infra
    arr["econ_infra"] = econ_infra
    arr["production"] = production
    arr["multisector"] = multisector
    arr["hum_aid"] = hum_aid
    arr["admin_expenses"] = admin_expenses
    arr["other"] = other
    
    out = json.dumps(arr)
    fjson.write(out)
    fcsv.close()
    fjson.close()
def country_centers():
    fcsv = open('country_centers.csv', 'rb')
    fjson = open('country_centers.json', 'wb')
    
    arr = {}
    headers = []
    
    line = fcsv.readline()
    lines = line.split('\r')
    headers = lines[0].split(',')
    print headers
    
    lines.pop(0)

    #
    ##for line in iter(lambda: fcsv.readline(), ""):
    for line in lines:
        arr1 = line.split(',')
        print arr1
        temp_dict = {}
        for x in range (1, len(headers)):
            print headers[x]
            print float(arr1[x])
            temp_dict[headers[x]] = float(arr1[x])
        arr[arr1[0]] = temp_dict
        
    out = json.dumps(arr)
    fjson.write(out)
    fcsv.close()
    fjson.close()

def donorcountryflows ():
    fcsv = open('net_oda.csv', 'rb')
    fjson = open('net_oda.json', 'wb')
    
    arr = {}
    headers = []
    
    line = fcsv.readline()
    lines = line.split('\r')
    headers = lines[0].split(',')
    print headers
    
    lines.pop(0)
    
    #
    ##for line in iter(lambda: fcsv.readline(), ""):
    for line in lines:
        arr1 = line.split(',')
        print arr1
        temp_dict = {}
#        for x in range (1, len(headers)):
#            temp_dict[headers[x]] = float(arr1[x])
#        arr[arr1[0]] = temp_dict
        arr[arr1[0]] = float(arr1[1])
    out = json.dumps(arr)
    fjson.write(out)
    fcsv.close()
    fjson.close()
donorcountryflows()