list = []
n = int(input('Enter the length of array:'))
if n % 2 == 0:
    print('No answer')
else:
    for i in range(n):
        list.append(input('Enter array Items:'))
    flag = 0
    i = 0
    while i <= (n // 2) + 1:
        if list[i] == list[n-1]:
            n -= 1
            i += 1
            flag = 1

    if flag == 1 :
        print('The entire array is symmetric')
    else:
        print('The entire array is not symmetric')
