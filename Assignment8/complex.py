a = complex((input('Enter the first complex number:')))
b = complex((input('Enter the second complex number:')))


choice = int(input('summation press 1, subtraction press 2, multiplication enter 3:'))
if choice == 1:
    print(a+b)
elif choice == 2:
    print(a-b)
elif choice == 3:
    print(a*b)
else:
    print('Enter a valid number')

