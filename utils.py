import random
from math import log, exp


def monteKarlo(strNum, a, b, c, d, e): # Фунция для создания данных для таблицы
    pMass = [('A', round(a, 4)), ('B', round(b, 4)),
             ('C', round(c, 4)), ('D', round(d, 4)),
            ('E', round(e, 4))] # создание списка со значениями пользователя 

    # создание списка с рандомными числами
    monteKarloTable = []
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

        # определение результата работы элементов
        for (name, num) in pMass:
            if monteKarloTable[i]['num'+name] > num:
                monteKarloTable[i]['result'+name] = '-'
            else:
                monteKarloTable[i]['result'+name] = '+'

        # определение результата работы блоков
        if monteKarloTable[i]["resultA"] == '+' or monteKarloTable[i]["resultB"] == '+' or monteKarloTable[i]["resultC"] == '+':
            monteKarloTable[i]["module1Work"] = '+'
        else:
            monteKarloTable[i]["module1Work"] = '-'

        if monteKarloTable[i]["resultD"] == '+' or monteKarloTable[i]["resultE"] == '+':
            monteKarloTable[i]["module2Work"] = '+'
        else:
            monteKarloTable[i]["module2Work"] = '-'

        # определение результата работы системы
        if monteKarloTable[i]["module1Work"] == '+' and monteKarloTable[i]["module2Work"] == '+':
            monteKarloTable[i]["system"] = '+'
        else:
            monteKarloTable[i]["system"] = '-'

    # переделываем список в нужный для таблицы формат 
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

    # вычисляем искомую надёжность системы (P*) 
    pluses = 0
    for row in monteKarloTable:
        if row["system"] == '+':
            pluses = pluses+1
    pStar = round(pluses/len(monteKarloTable), 4)

    # вычисляем надёжность каждого блока и всей системы аналитически(P1, P2 и P)
    p1 = round((1-(1-a)*(1-b)*(1-c)), 4)
    p2 = round((1-(1-d)*(1-e)), 4)
    p = round(p1*p2, 4)

    # Дополняем таблицу строкой с результатами вычислений и определяем абсолютную погрешность (|P-P*|)
    newMonteKarloTable.append([None, None, None, None, None, None, '(stop)', None, None,
                               f'P<sub>1</sub> = {p1}',
                               f'P<sub>2</sub> = {p2}',
                               f'P = {p}',
                               f'P* = {pStar}',
                               f'|P-P*| = {round(abs(p - pStar), 4)}'])
    return newMonteKarloTable

def getQuantityOfListElements(thisList): # Функция для вычисления кол-ва элементов
    counter = 0
    if isinstance(thisList, list):
        for element in thisList:
            counter += getQuantityOfListElements(element)
    else:
        counter += 1
    return counter

def checkMonteKarloTable(monteKarloTable, strNum): # Функция с проверкой на формат таблицы
    strCounter = 0;
    for str in monteKarloTable:
        strCounter+=1

    if getQuantityOfListElements(monteKarloTable) == strNum*14 and strNum == strCounter:
        return True
    else:
        return False

def get_tau(a, r):
    ln_r = log(r, exp(1))
    tau = a * ln_r
    return (tau, ln_r)



