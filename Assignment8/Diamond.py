a = int(input('Enter the number of rows:'))
for i in range (int(a/2)) :
    print(((int(a/2)-1) - i) *' ',(2*i - 1) * '*' , end='')
    print()
for j in reversed(range(int(a/2 - 1 ))):
    print(((int(a/2)-1) - j) *' ',(2*j - 1) * '*' , end='')
    print()