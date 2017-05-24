#!/Users/abombard/.brew/bin/python

import sys, csv

if len(sys.argv) != 2 and len(sys.argv) != 3:
    print "Usage: " + sys.argv[0] + " [-g|-l] <km>"
    sys.exit()

method = "-g"
if len(sys.argv) == 3:
    method = sys.argv[1]
    if method != "-g" and method != "-l":
        print "Usage: " + sys.argv[0] + " [-g|-l] <km>"
        sys.exit()

try:
    if len(sys.argv) == 2:
        km = float(sys.argv[1])
    else:
        km = float(sys.argv[2])
except:
    print "Usage: " + sys.argv[0] + " [-g|-l] <km>"
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
