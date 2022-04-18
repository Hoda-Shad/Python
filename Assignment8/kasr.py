def mul(x, y):
    result = {}
    result['s'] = x['s'] * y['s']
    result['m'] = x['m'] * y['m']
    return result


def sum(x, y):
    result = {'s': x['s'] * y['m'] + y['s'] * x['m'], 'm': x['m'] * y['m']}
    return result

def sub(x,y):
    result = {}
    result['s'] = x['s'] * y['m'] - y['s'] * x['m']
    result['m'] = x['m'] * y['m']
    return result


def div(x,y):
    result = {}
    result['s'] = x['s'] * y['m']
    result['m'] = x['m'] * y['s']
    return result


def show(x):
     print(x['s'], '/' , x['m'])


a = {'s': 2, 'm': 3}
b = {'s': 5, 'm': 4}
c = mul(a, b)
d = sum(a, b)
e = sub(a, b)
d = div(a, b)
show(c)
show(d)
show(e)
show(d)