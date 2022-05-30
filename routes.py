import math
from utils import monteKarlo, monteKarloRemake
from bottle import post, request, view, get


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
        'title': 'First Variant',
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

    A = float(request.forms.get('numA'))
    B = float(request.forms.get('numB'))
    C = float(request.forms.get('numC'))
    D = float(request.forms.get('numD'))
    E = float(request.forms.get('numE'))
    rowCount = int(request.forms.get('rowCount'))
    rows = monteKarloRemake(monteKarlo(rowCount,A,B,C,D,E))
    #rows.append(['Итого',None,None,None,None,None,None,None,None,None,None,None,None,None])

    return {'ok': rows}


@post('/api/second_variant')
def second_variant_api():
    from time import sleep
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


@post('/api/third_variant')
def third_variant_api():
    from time import sleep
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
            '4',
            '1',
            '2',
        ])

        total += current

    sleep(.5)

    return {'ok': rows}
