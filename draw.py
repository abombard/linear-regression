#!/Users/abombard/.brew/bin/python

import sys, csv

from plotly.offline import plot
import plotly.graph_objs as go

import file

if len(sys.argv) != 1 and len(sys.argv) != 2:
    print "Usage: " + sys.argv[0] + " [-g|-l]>"
    sys.exit()

method = "-g"
if len(sys.argv) == 2:
    method = sys.argv[1]
    if method != "-g" and method != "-l":
        print "Usage: " + sys.argv[0] + " [-g|-l]>"
        sys.exit()

datas = file.readDatasFromCsv()
teta0, teta1 = file.readTetasFromCsv()

xList = [x for x, y in datas]
yList = [y for x, y in datas]

points = [go.Scatter(x = xList, y = yList, mode = 'markers')]

def scaleData(v, minV, maxV):
    return (v - minV) / (maxV - minV)

minKm = min(datas,key=lambda item:item[0])[0]
maxKm = max(datas,key=lambda item:item[0])[0]

if method == "-g":
    x0 = minKm
    y0 = teta0 + teta1 * scaleData(x0, minKm, maxKm)
    x1 = maxKm
    y1 = teta0 + teta1 * scaleData(x1, minKm, maxKm)
elif method == "-l":
    x0 = minKm
    y0 = teta0 + teta1 * x0
    x1 = maxKm
    y1 = teta0 + teta1 * x1

layout = {
    'shapes': [
    {
        'type': 'line',
        'x0': x0,
        'y0': y0,
        'x1': x1,
        'y1': y1,
        'line': {
            'color': 'rgb(55, 128, 191)',
            'width': 3,
        },
    }]
}

fig = {
    'data': points,
    'layout': layout
}

plot(fig, filename='graph.html')
