from bottle import post, request, view, get
from datetime import datetime
from time import sleep
from json import dump
import os

from parsers import parse_sv_tv
from utils import monteKarlo, checkMonteKarloTable, ROUND_DIGITS, third_variant_calc, get_tau, get_rand


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
    # TODO Make validations
    # Describes how long request will take time to be processed
    t1 = float(request.forms.get('t1'))
    # How long to run algorithm
    t2 = float(request.forms.get('t2'))
    # Multiplier for TAU
    a = float(request.forms.get('a'))

    rows = []
    passed = 1
    refused = 0
    c = [t1, 0, 0]
    count = 1
    total_time = 0

    c1 = total_time + t1
    rows.append([
        count,
        '-',
        '-',
        '-  ',
        total_time,
        c1,
        '-',
        '-',
        '+',
        '-',
    ])

    while True:
        channel = -1
        passes = True
        count += 1
        r = get_rand()
        (ln_r, tau) = get_tau(a, r)
        #Stop
        total_time = round(total_time + tau, ROUND_DIGITS)
        if (total_time / 60) > t2 or count > 1000000:
            break

        for i in range(3):
            if c[i] <= total_time:
                channel = i
                c[i] = round(total_time + t1, ROUND_DIGITS)
                break
        else:
            refused += 1
            passes = False

        rows.append([
            count,
            r,
            ln_r,
            tau,
            total_time,
            c[0] if channel == 0 else '-',
            c[1] if channel == 1 else '-',
            c[2] if channel == 2 else '-',
            '+' if passes else '-',
            '-' if passes else '+'
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
        f'X<sub>i</sub>={passed}',
        f'refused={refused}'
    ])

    with open(f'./second_variant_results_tv.log', 'a') as file:
        file.write("\n")
        dump({
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "t1": t1,
            "t2": t2,
            "a": a,
        }, file)

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
    with open(f'./results_tv.log', 'a') as file:
        file.write("\n")
        dump({
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "t1": t1,
            "t2": t2,
            "a": a,
        }, file)

    sleep(.5)

    return {'ok': rows}
