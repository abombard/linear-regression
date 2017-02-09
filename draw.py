import sys, csv

from plotly.offline import plot
import plotly.graph_objs as go

def readDatasFromCsv(filename):
    datas = []

    try:
        with open(filename, 'rb') as datafile:
            reader = csv.reader(
                datafile,
                delimiter=',',
                quotechar='|'
            )
            junk = next(reader)

            for km, price in reader:
                datas.append((float(km), float(price)))
    except:
        print filename, "is unreachable"
        sys.exit(1)
    
    return datas

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


datas = readDatasFromCsv('data.csv')
teta0, teta1 = readTetasFromCsv('teta.csv')

xList = [x for x, y in datas]
yList = [y for x, y in datas]

points = [go.Scatter(x = xList, y = yList, mode = 'markers')]

x0 = 22899
y0 = teta0 + teta1 * x0
x1 = 240000
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
