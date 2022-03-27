import numpy as np
a = int(input('Enter a number: '))
A = np.zeros((a,a), dtype =int)

A[:,0] = 1
for k in range (a):
    for i in range (1,a):
        for j in range (1,a):
            A[i][j]= A[i-1][j-1] + A[i-1][j]
for i in range(a):
    for j in range(a):
        if A[i][j] != 0:
            print(A[i][j], end=' ')
    print()