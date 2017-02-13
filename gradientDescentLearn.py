#!/usr/bin/python

import sys, csv
import file

learningRate = 1.0
maxiteration = 100

def scaleData(v, minV, maxV):
    return (v - minV) / (maxV - minV)

def scaleDatas(datas):
    scaledDatas = []

    minKm = min(datas,key=lambda item:item[0])[0]
    maxKm = max(datas,key=lambda item:item[0])[0]

    for km, price in datas:
        newKm = scaleData(km, minKm, maxKm)
        scaledDatas.append((newKm, price))

    return minKm, maxKm, scaledDatas

def stepGradient(teta0, teta1, datas, learningRate):
    teta0_gradient = 0
    teta1_gradient = 0
    M = float(len(datas))
    for km, price in datas:
        priceDiff = teta0 + (teta1 * km) - price
        teta0_gradient += priceDiff
        teta1_gradient += priceDiff * km
    teta0 = teta0 - (learningRate / M * teta0_gradient)
    teta1 = teta1 - (learningRate / M * teta1_gradient)
    return teta0, teta1

# main
teta0, teta1 = file.readTetasFromCsv()
datas = file.readDatasFromCsv()

# scale
minKm, maxKm, datas = scaleDatas(datas)

# gradient descend
for i in range(maxiteration):
    teta0, teta1 = stepGradient(teta0, teta1, datas, learningRate)

file.writeTetasToCsv(teta0, teta1)

