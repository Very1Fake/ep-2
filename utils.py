import random
def monteKarlo(strNum,A,B,C,D,E):

    moduleWork = []
    P = [('A', A), ('B', B),('C', C), ('D', D), ('E', E)]

    for i in range(0,strNum,1):
        moduleWork.append({"Anum":round(random.random(), 4),
                           "Bnum":round(random.random(), 4),
                           "Cnum":round(random.random(), 4),
                           "Dnum":round(random.random(), 4),
                           "Enum":round(random.random(), 4),
                           "Aresult": None,
                           "Bresult": None,
                           "Cresult": None,
                           "Dresult":None,
                           "Eresult": None,
                           "module1Work":None,
                           "module2Work":None,
                           "system":None});
    

    for work in moduleWork:
        for (name, num) in P:
            if work[name + 'num'] > num:
                work[name+'result'] = '-'
            else:
                work[name+'result'] = '+'
        
            if (work["Aresult"] == '+' or work["Bresult"] == '+' or work["Cresult"] == '+'):
                work["module1Work"] = '+'
            else:
                work["module1Work"] = '-'

            if (work["Dresult"] == '+' or work["Eresult"] == '+'):
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
            pluses=pluses+1
    return pluses/len(monteKarloTable)

def reliabAnalitic_1Module(A,B,C):
    return 1-(1-A)*(1-B)*(1-C)

def reliabAnalitic_2Module(D,E):
    return 1-(1-D)*(1-E)

def monteKarloRemake(monteKarloTable):
    newMonteKarloTable = []
    for row in range(0,len(monteKarloTable),1):
        newMonteKarloTable.append([
            row+1,
            f'First<br>Second',
            monteKarloTable[row]["Anum"],
            monteKarloTable[row]["Bnum"],
            monteKarloTable[row]["Cnum"],
            monteKarloTable[row]["Dnum"],
            monteKarloTable[row]["Enum"],
            f'{monteKarloTable[row]["Aresult"]}<br>',
            f'{monteKarloTable[row]["Bresult"]}<br>',
            f'{monteKarloTable[row]["Cresult"]}<br>',
            f'<br>{monteKarloTable[row]["Dresult"]}',
            f'<br>{monteKarloTable[row]["Eresult"]}',
            f'{monteKarloTable[row]["module1Work"]}<br>{monteKarloTable[row]["module2Work"]}',
            monteKarloTable[row]["system"]
        ])
    return newMonteKarloTable

print(monteKarloRemake(monteKarlo(5,0.6,0.6,0.6,0.6,0.6)))
