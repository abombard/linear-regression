#!/Users/abombard/.brew/bin/python

import sys, csv
import file

datas = file.readDatasFromCsv()

N = len(datas)
Exy = sum([(x * y) for x, y in datas])
Ex = sum([x for x, y in datas])
Ey = sum([y for x, y in datas])
ExSquare = sum([x ** 2 for x, y in datas])

teta1 = (Exy - (Ex * Ey) / N ) / (ExSquare - (Ex ** 2 / N))
teta0 = (Ey - (teta1 * Ex)) / N

file.writeTetasToCsv(teta0, teta1)
