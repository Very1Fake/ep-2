from bottle import post, request, view, get
from datetime import datetime
from time import sleep
from json import dump
import os

from parsers import parse_sv_tv
from utils import monteKarlo, checkMonteKarloTable, ROUND_DIGITS, third_variant_calc


@get('/')
@view('index')
def index():
    return


@get('/about')
@view('about')
def about():
    return


@get('/first_variant')
@view('variant')
def first_variant():
    return {
        'title': 'First Variant: evaluation of the reliability of the simplest systems by the Monte Carlo method',
        'link': '/first_variant',
        'variant': 1,
    }


@get('/second_variant')
@view('variant')
def second_variant():
    return {
        'title': 'Second Variant',
        'link': '/second_variant',
        'variant': 2,
    }


@get('/third_variant')
@view('variant')
def third_variant():
    return {
        'title': 'Third Variant',
        'link': '/third_variant',
        'variant': 3,
    }


@post('/api/first_variant')
def first_variant_api():
    # Получение значений от пользователя
    a = float(request.forms.get('numA'))
    b = float(request.forms.get('numB'))
    c = float(request.forms.get('numC'))
    d = float(request.forms.get('numD'))
    e = float(request.forms.get('numE'))
    countOfTests = int(request.forms.get('rowCount'))
    rows = monteKarlo(countOfTests, a, b, c, d, e)

    # Запись данных пользователя в текстовый файл
    with open(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')+"/monteKarloHistr.txt", "a+") as file:
        file.write(str(datetime.now())+'; countOfTests:'+str(countOfTests)+'; A:' +
                   str(a)+'; B:'+str(b)+'; C:'+str(c)+'; D:'+str(d)+'; E:'+str(e)+'\n')

    # Проверка на формат таблицы
    if checkMonteKarloTable(rows, (countOfTests+1)) == False:
        return None

    return {'ok': rows}


@post('/api/second_variant')
def second_variant_api():
    import random  # FIX

    # TODO Make validations
    t1 = float(request.forms.get('t1'))
    t2 = float(request.forms.get('t2'))
    a = int(request.forms.get('a'))

    rows = []
    total = 0

    for row in range(a):
        current = random.random()

        rows.append([
            row + 1,
            round(random.random(), 2),
            round(random.random(), 2),
            round(total - current, 3),
            round(total, 3),
            round(total + t1, 3),
            '2',
            '3',
            '1',
            '2',
        ])

        total += current

    sleep(.5)

    return {'ok': rows}


# API route for third variant
@post('/api/third_variant')
def third_variant_api():
    args = parse_sv_tv(
        # Describes how long request will take time to be processed
        request.forms.get('t1'),
        # How long to run algorithm
        request.forms.get('t2'),
        # Multiplier for TAU
        request.forms.get('a'),
    )

    # Handle error from validation
    if isinstance(args, str):
        return {'error': args}
    else:
        (t1, t2, a) = args

    rows = third_variant_calc(t1, t2, a)

    # Save result to file
    now = datetime.now()
    with open(f'./results_tv/result_{now.strftime("%Y-%m-%d_%H:%M:%S")}.json', 'w+') as file:
        dump({
            "date": now.strftime("%Y-%m-%d %H:%M:%S"),
            "rows": rows,
        }, file)

    sleep(.5)

    return {'ok': rows}
