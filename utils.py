import random
from math import log, exp


def monteKarlo(strNum, a, b, c, d, e):

    moduleWork = []
    P = [('A', a), ('B', b), ('C', c), ('D', d), ('E', e)]

    for i in range(0, strNum, 1):
        moduleWork.append({"numA": round(random.random(), 4),
                           "numB": round(random.random(), 4),
                           "numC": round(random.random(), 4),
                           "numD": round(random.random(), 4),
                           "numE": round(random.random(), 4),
                           "resultA": None,
                           "resultB": None,
                           "resultC": None,
                           "resultD": None,
                           "resultE": None,
                           "module1Work": None,
                           "module2Work": None,
                           "system": None})

    for work in moduleWork:
        for (name, num) in P:
            if work['num'+name] > num:
                work['result'+name] = '-'
            else:
                work['result'+name] = '+'

        if (work["resultA"] == '+' or work["resultB"] == '+' or work["resultC"] == '+'):
            work["module1Work"] = '+'
        else:
            work["module1Work"] = '-'

        if (work["resultD"] == '+' or work["resultE"] == '+'):
            work["module2Work"] = '+'
        else:
            work["module2Work"] = '-'

        if(work["module1Work"] == '+' and work["module2Work"] == '+'):
            work["system"] = '+'
        else:
            work["system"] = '-'

    return moduleWork


def relativeFrequecy(monteKarloTable):
    pluses = 0
    for row in monteKarloTable:
        if row["system"] == '+':
            pluses = pluses+1
    return pluses/len(monteKarloTable)


def reliabAnalitic_1Module(A, B, C):
    return 1-(1-A)*(1-B)*(1-C)


def reliabAnalitic_2Module(D, E):
    return 1-(1-D)*(1-E)


def monteKarloRemake(monteKarloTable, a, b, c, d, e):
    newMonteKarloTable = []
    for row in range(0, len(monteKarloTable), 1):
        newMonteKarloTable.append([
            row+1,
            f'First<br>Second',
            monteKarloTable[row]["numA"],
            monteKarloTable[row]["numB"],
            monteKarloTable[row]["numC"],
            f'<br>{monteKarloTable[row]["numD"]}',
            f'<br>{monteKarloTable[row]["numE"]}',
            f'{monteKarloTable[row]["resultA"]}<br>',
            f'{monteKarloTable[row]["resultB"]}<br>',
            f'{monteKarloTable[row]["resultC"]}<br>',
            f'<br>{monteKarloTable[row]["resultD"]}',
            f'<br>{monteKarloTable[row]["resultE"]}',
            f'{monteKarloTable[row]["module1Work"]}<br>{monteKarloTable[row]["module2Work"]}',
            monteKarloTable[row]["system"]
        ])
    p = round(round(reliabAnalitic_1Module(a, b, c), 4)
              * round(reliabAnalitic_2Module(d, e), 4), 4)
    newMonteKarloTable.append([None, None, None, None, None, None, '(stop)', None, None,
                               f'P<sub>1</sub> = {round(reliabAnalitic_1Module(a, b, c),4)}',
                               f'P<sub>2</sub> = {round(reliabAnalitic_2Module(d, e),4)}',
                               f'P = {p}',
                               f'P* = {round(relativeFrequecy(monteKarloTable), 4)}',
                               f'|P-P*| = {abs(round(p - relativeFrequecy(monteKarloTable), 4))}'])
    return newMonteKarloTable


def get_tau(a, r):
    ln_r = log(r, exp(1))
    tau = a * ln_r
    return (tau, ln_r)
