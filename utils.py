import random
from math import log, exp

def monteKarlo(strNum, a, b, c, d, e):
    monteKarloTable = []
    pMass = [('A', round(a, 4)), ('B', round(b, 4)),
             ('C', round(c, 4)), ('D', round(d, 4)), ('E', round(e, 4))]

    for i in range(0, strNum, 1):
        monteKarloTable.append({"numA": round(random.random(), 4),
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

        for (name, num) in pMass:
            if monteKarloTable[i]['num'+name] > num:
                monteKarloTable[i]['result'+name] = '-'
            else:
                monteKarloTable[i]['result'+name] = '+'

        if monteKarloTable[i]["resultA"] == '+' or monteKarloTable[i]["resultB"] == '+' or monteKarloTable[i]["resultC"] == '+':
            monteKarloTable[i]["module1Work"] = '+'
        else:
            monteKarloTable[i]["module1Work"] = '-'

        if monteKarloTable[i]["resultD"] == '+' or monteKarloTable[i]["resultE"] == '+':
            monteKarloTable[i]["module2Work"] = '+'
        else:
            monteKarloTable[i]["module2Work"] = '-'

        if monteKarloTable[i]["module1Work"] == '+' and monteKarloTable[i]["module2Work"] == '+':
            monteKarloTable[i]["system"] = '+'
        else:
            monteKarloTable[i]["system"] = '-'

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

    pluses = 0
    for row in monteKarloTable:
        if row["system"] == '+':
            pluses = pluses+1
    pStar = round(pluses/len(monteKarloTable), 4)

    p1 = round((1-(1-a)*(1-b)*(1-c)), 4)
    p2 = round((1-(1-d)*(1-e)), 4)
    p = round(p1*p2, 4)

    newMonteKarloTable.append([None, None, None, None, None, None, '(stop)', None, None,
                               f'P<sub>1</sub> = {p1}',
                               f'P<sub>2</sub> = {p2}',
                               f'P = {p}',
                               f'P* = {pStar}',
                               f'|P-P*| = {abs(p - pStar)}'])


def get_tau(a, r):
    ln_r = log(r, exp(1))
    tau = a * ln_r
    return (tau, ln_r)
