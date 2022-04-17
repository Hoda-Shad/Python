def standard_of_time(t):
    print('your time is', '\n', t['h'], ':', t['m'], ':', t['s'])
    while t['s'] >= 60:
        t['s'] -= 60
        t['m'] += 1
    while t['m'] >= 60:
        t['m'] -= 60
        t['h'] += 1
    while t['s'] < 0:
        t['s'] += 60
        t['m'] -= 1
    while t['m'] < 0:
        t['m'] += 60
        t['h'] -= 1
    print('The standard time is','\n', t['h'],':',t['m'] ,':',t['s'])

def sum_of_time(t0,t1):
    t2 = {}
    t2['s'] = t1['s'] + t0['s']
    t2['m'] = t1['m'] + t0['m']
    t2['h'] = t1['h'] + t0['h']
    standard_of_time(t2)

def sub_of_time(t0,t1):
    t2 = {}
    t2['s'] = t1['s'] - t0['s']
    t2['m'] = t1['m'] - t0['m']
    t2['h'] = t1['h'] - t0['h']
    standard_of_time(t2)

def input_time():
    t0 = {}
    t1 = {}
    t0['s'] = int(input('Enter the seconds:'))
    t0['m'] = int(input('Enter the minutes:'))
    t0['h'] = int(input('Enter the houres:'))
    t1['s'] = int(input('Enter the seconds:'))
    t1['m'] = int(input('Enter the minutes:'))
    t1['h'] = int(input('Enter the houres:'))
    return(t0,t1)

def convert_second_time():
    t = {}
    t['s'] = int(input('Enter seconds:'))
    t['m'] = 0
    t['h'] = 0
    while (t['s'] >= 60):
        t['m'] = t['s'] // 60
        t['s'] = t['s'] % 60
        while t['m'] >= 60:
            t['m'] -= 60
            t['h'] += 1
    print('The standard time is','\n', t['h'] ,':', t['m'] ,':', t['s'])


def convert_time_second():
    input_time = input('Enter time:')
    list = input_time.split(':')
    print(list)
    seconds = int(list[0]) * 3600 + int(list[1]) * 60 + int(list[2])
    print('Tne entire time is ', seconds , 'seconds')


choice = int (input ('summation press 1, subtraction press 2, for convet second to time press 3, for convert time to second enter4:'))
if choice == 1 :
    t0 , t1 = input_time()
    sum_of_time(t0, t1)
elif choice == 2 :
    t0, t1 = input_time()
    sub_of_time(t0, t1)
elif choice == 3:
    convert_second_time()
elif choice == 4:
     convert_time_second()
else:
    print('Enter a valid number')
