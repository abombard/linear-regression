import sys, csv

from plotly.offline import plot
import plotly.graph_objs as go

import file

datas = file.readDatasFromCsv()
teta0, teta1 = file.readTetasFromCsv()

xList = [x for x, y in datas]
yList = [y for x, y in datas]

points = [go.Scatter(x = xList, y = yList, mode = 'markers')]

def scaleData(v, minV, maxV):
    return (v - minV) / (maxV - minV)

minKm = min(datas,key=lambda item:item[0])[0]
maxKm = max(datas,key=lambda item:item[0])[0]

x0 = minKm
y0 = teta0 + teta1 * scaleData(x0, minKm, maxKm)
x1 = maxKm
y1 = teta0 + teta1 * scaleData(x1, minKm, maxKm)

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
