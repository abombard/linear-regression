#!/usr/bin/python

import sys, csv

learningRate = 0.5
maxiteration = 100

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

def scaleData(v, minV, maxV):
    return (v - minV) / (maxV - minV)

def scaleDatas(datas, minV, maxV):
    scaledDatas = []

    for km, price in datas:
        newKm = scaleData(km, minKm, maxKm)
        scaledDatas.append((newKm, price))

    return scaledDatas

def stepGradient(teta0, teta1, datas, learningRate):
    teta0_gradient = 0
    teta1_gradient = 0
    M = float(len(datas))
    for km, price in datas:
        estimatePrice = teta0 + (teta1 * km)
        teta0_gradient += (estimatePrice - price)
        teta1_gradient += ((estimatePrice - price) * km)
    new_teta0 = teta0 - (learningRate / M * teta0_gradient)
    new_teta1 = teta1 - (learningRate / M * teta1_gradient)
    return new_teta0, new_teta1

# main
teta0, teta1 = readTetasFromCsv('teta.csv')
datas = readDatasFromCsv('data.csv')

minKm = min(datas,key=lambda item:item[0])[0]
maxKm = max(datas,key=lambda item:item[0])[0]

datas = scaleDatas(datas, minKm, maxKm)

for i in range(maxiteration):
    teta0, teta1 = stepGradient(teta0, teta1, datas, learningRate)

teta1 = teta1 / (maxKm - minKm)

writeTetasToCsv('teta.csv', teta0, teta1)

