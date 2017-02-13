import sys, csv

def readTetasFromCsv():
    try:
        with open('teta.csv', 'r') as csvfile:
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

def writeTetasToCsv(teta0, teta1):

    with open('teta.csv', 'w') as datafile:
        writer = csv.writer(
            datafile,
            delimiter=',',
            quotechar='|',
            quoting=csv.QUOTE_NONE
        )
        writer.writerow(['teta0', 'teta1'])
        writer.writerow([teta0, teta1])

def readDatasFromCsv():
    datas = []

    try:
        with open('data.csv', 'r') as datafile:
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

