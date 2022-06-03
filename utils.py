from random import random
from math import log, exp

ROUND_DIGITS = 5
RANDOM_RETRIES = 16


def monteKarlo(strNum, a, b, c, d, e):  # Фунция для создания данных для таблицы
    pMass = [('A', round(a, 4)), ('B', round(b, 4)),
             ('C', round(c, 4)), ('D', round(d, 4)),
             ('E', round(e, 4))]  # создание списка со значениями пользователя

    # создание списка с рандомными числами
    monteKarloTable = []
    for i in range(0, strNum, 1):
        monteKarloTable.append({"numA": round(random(), 4),
                                "numB": round(random(), 4),
                                "numC": round(random(), 4),
                                "numD": round(random(), 4),
                                "numE": round(random(), 4),
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


# Функция для вычисления кол-ва элементов
def getQuantityOfListElements(thisList):
    counter = 0
    if isinstance(thisList, list):
        for element in thisList:
            counter += getQuantityOfListElements(element)
    else:
        counter += 1
    return counter


# Функция с проверкой на формат таблицы
def checkMonteKarloTable(monteKarloTable, strNum):
    strCounter = 0
    for str in monteKarloTable:
        strCounter += 1

    if getQuantityOfListElements(monteKarloTable) == strNum*14 and strNum == strCounter:
        return True
    else:
        return False


def third_variant_calc(t1, t2, a):
    rows = []
    passed = 1
    c = [0, 0, 0, 0]
    count = 1
    total_time = 0

    c1 = total_time + t1
    rows.append([
        count,
        '',
        '',
        '',
        total_time,
        c1,
        '',
        '',
        '',
        '1',
    ])

    while True:
        channel = -1
        passes = True
        count += 1
        r = get_rand()
        (ln_r, tau) = get_tau(a, r)

        total_time = round(total_time + tau, ROUND_DIGITS)

        for i in range(4):
            if c[i] <= total_time:
                channel = i
                c[i] = round(total_time + t1, ROUND_DIGITS)
                break
        else:
            nearest = c.index(min(c))
            total_time = c[nearest]
            c[nearest] = round(total_time + t1, ROUND_DIGITS)
            channel = nearest

        rows.append([
            count,
            r,
            ln_r,
            tau,
            total_time,
            c[0] if channel == 0 else '-',
            c[1] if channel == 1 else '-',
            c[2] if channel == 2 else '-',
            c[3] if channel == 3 else '-',
            '1' if passes else '-',
        ])

        if passes:
            passed += 1
        if (total_time / 60) > t2 or count > 1000:
            break

    rows.append([
        '',
        '',
        '',
        '',
        '&lt;stop&gt;',
        '',
        '',
        '',
        '',
        f'X<sub>i</sub>={passed}',
    ])

    return rows


def get_rand() -> float:
    for i in range(RANDOM_RETRIES):
        r = round(random(), ROUND_DIGITS)

        if r != 0.0:
            return r
    else:
        raise Exception


def get_tau(a, r):
    ln_r = round(-log(r, exp(1)), ROUND_DIGITS)
    tau = round(a * ln_r, ROUND_DIGITS)
    return (tau, ln_r)
