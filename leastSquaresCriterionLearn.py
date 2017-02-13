#!/usr/bin/python

import sys, csv

def writeTetasToCsv(filename, teta0, teta1):

    with open('teta.csv', 'wb') as datafile:
        writer = csv.writer(
            datafile,
            delimiter=',',
            quotechar='|',
            quoting=csv.QUOTE_NONE
        )
        writer.writerow(['teta0', 'teta1'])
        writer.writerow([teta0, teta1])

def readDatasFromCsv(filename):
    datas = []

    try:
        with open('data.csv', 'rb') as datafile:
            reader = csv.reader(
                datafile,
                delimiter=',',
                quotechar='|'
            )
            junk = next(reader)

            for km, price in reader:
                datas.append((float(km), float(price)))
    except:
        print "datas.csv is unreachable"
        sys.exit(1)
    
    return datas

# main
datas = readDatasFromCsv('data.csv')

N = len(datas)
Exy = sum([(x * y) for x, y in datas])
Ex = sum([x for x, y in datas])
Ey = sum([y for x, y in datas])
ExSquare = sum([x ** 2 for x, y in datas])

teta1 = (Exy - (Ex * Ey) / N ) / (ExSquare - (Ex ** 2 / N))
teta0 = (Ey - (teta1 * Ex)) / N

writeTetasToCsv('teta.csv', teta0, teta1)
