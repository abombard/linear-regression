#!/usr/bin/python

import sys, csv

try:
    km = float(sys.argv[1])
except:
    print "Usage: " + sys.argv[0] + " <km>"
    sys.exit(2)

import file

teta0, teta1 = file.readTetasFromCsv()
datas = file.readDatasFromCsv()

def scaleData(v, minV, maxV):
    return (v - minV) / (maxV - minV)

minKm = min(datas,key=lambda item:item[0])[0]
maxKm = max(datas,key=lambda item:item[0])[0]

price = teta0 + (teta1 * scaleData(km, minKm, maxKm))

print price
