#!/usr/bin/python

import sys, csv

try:
    km = float(sys.argv[1])
except:
    print "Usage: " + sys.argv[0] + " <km>"
    sys.exit(2)

def readTetasFromCsv(filename):
    try:
        with open('teta.csv', 'rb') as csvfile:
            spamreader = csv.reader(
                    csvfile,
                    delimiter=',',
                    quotechar='|'
            )
            row1 = next(spamreader)
            row2 = next(spamreader)

            teta0 = float(row2[0])
            teta1 = float(row2[1])
    except:
        teta0 = 0
        teta1 = 0

    return float(teta0), float(teta1)

teta0, teta1 = readTetasFromCsv('teta.csv')
price = float(teta0 + (teta1 * km))

print price
