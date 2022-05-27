import math

from bottle import post, request, view, get

@get('/')
@view('index')
def index():
    return

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
            '',
            '',
            '',
            '',
        ])

        total += current

    sleep(.5)

    return {'ok': rows}
