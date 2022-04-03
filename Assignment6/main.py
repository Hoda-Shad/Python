from pyfiglet import Figlet
import qrcode

RRODUCT = []
flag = 1


def ADD():
    new_product = input('Enter product Code, Name , Price, Amount: ')
    new_product = new_product.replace(' ', ',')
    myfile = open('database', 'a')
    myfile.write('\n')
    myfile.write(new_product)
    # myfile = open('database', 'r')
    # print('myfile.read()')
    print('your product added successfully')


def QRCODE():
    product_id = int(input("Enter product id:"))
    img = qrcode.make(product_id)
    img.save('qrcode.png')


def SEARCH():
    product_name = input("Enter product name:")
    for i in range(len(RRODUCT)):
        if RRODUCT[i]['name'] == product_name:
            print(RRODUCT[i])
            return i
    print('There is no product with Entire name')


# def EDIT():
#     product_name = input("Enter product name:")
#     for i in range(len(RRODUCT)):
#         if RRODUCT[i]['name'] == product_name:
#             print(RRODUCT[i])
#         number = int(input('For edit ID input 0, NAME input 1, PRICE input 2, COUNT input 3: '))
#         if number == 0:
#             product_newid = int(input("Enter product new id:"))
#             RRODUCT[i]['id'] = product_newid
#         elif number == 1:
#             product_newname = input("Enter product new name:")
#             RRODUCT[i]['name'] = product_newname
#         elif number == 2:
#             product_newprice = int(input("Enter product new price:"))
#             RRODUCT[i]['price'] = product_newprice
#         elif number == 3:
#             product_newcount = int(input("Enter product new count:"))
#             RRODUCT[i]['count'] = product_newcount
#         myfile = open('database', 'r')
#         print(myfile.readline(i))
#         # myfile.writelines([RRODUCT[i]])

def EDIT():
    index = SEARCH()
    # print(index)
    if index is not None:
        file = open("database", "r")
        list_of_lines = file.readlines()
        list_of_lines[index] = input("enter id , name , price , number of product: ") + '\n'
        list_of_lines[index] = list_of_lines[index].replace(" ", ",")
        a_file = open("database", "w")
        a_file.writelines(list_of_lines)
        a_file.close()
    else:
        print('item not found!')

def DELETE():
    i = SEARCH()
    RRODUCT[i].clear()
    myfile = open("database.txt", "w")
    myfile.writelines(RRODUCT[i])
    print(RRODUCT)


def load():
    print('Loading...')
    myfile = open('database', 'r')
    data = myfile.read()
    product_list = data.split('\n')
    for i in range(len(product_list)):
        product_info = product_list[i].split(',')
        mydict = {}
        mydict['id'] = int(product_info[0])
        mydict['name'] = product_info[1]
        mydict['price'] = int(product_info[2])
        mydict['count'] = int(product_info[3])
        RRODUCT.append(mydict)
    print('Welcome')

def SAVE():
        myfile = open('database', 'w')
        for i in range(len(RRODUCT)):
            myfile.write(str(RRODUCT[i]['id']))
            myfile.write(',')
            myfile.write((RRODUCT[i]['name']))
            myfile.write(',')
            myfile.write(str(RRODUCT[i]['price']))
            myfile.write(',')
            myfile.write(str(RRODUCT[i]['count']))
            myfile.write('\n')
            # row = str(RRODUCT[i]['id']) + ',' + RRODUCT[i]['name'] + ',' + str(RRODUCT[i]['price']) + ',' + str(RRODUCT[i]['count'] + '\n')
            # myfile.write(row)
        myfile.close()
        exit


def BUY():
    flag = 1
    basket = []
    total = 0
    while input('for exit press * for continue press Enter') != '*':
        product_id = int(input("Enter the product id:"))
        for i in range(len(RRODUCT)):
            if RRODUCT[i]['id'] == product_id:
                flag = 0
                if RRODUCT[i]['count'] == 0:
                    print('The product isnot available')
                    break
                else:
                    product_count = int(input("How many do you need? "))
                    if int(product_count) > int(RRODUCT[i]['count']):
                        print('Inventory is not enough you can buy up to', RRODUCT[i]['count'], 'number')
                        break
                    else:
                        RRODUCT[i]['count'] = RRODUCT[i]['count'] - product_count
                        basket.append(RRODUCT[i]['name'])
                        file = open("database", "r")
                        list_of_lines = file.readlines()
                        list_of_lines[i] = list_of_lines[i].split(',')
                        list_of_lines[i][3] = RRODUCT[i]['count']
                        list_of_lines[i] = str(
                            list_of_lines[i][0] + ',' + list_of_lines[i][1] + ',' + list_of_lines[i][
                                2] + ',' + str(list_of_lines[i][3])) + '\n'
                        a_file = open("database", "w")
                        a_file.writelines(list_of_lines)
                        a_file.close()
                        total += product_count * RRODUCT[i]['price']
                        print('This Item added tp your basket successfully ')
        if flag == 1:
            print('There is no product with this id')
    print("your current basket is : ", basket)
    print('your factor = ', total)


def show_list():
    for i in range(len(RRODUCT)):
        print(RRODUCT)


f = Figlet(font='standard')
print(f.renderText('Hoda Store'))


def showmenu():
    print('1- Add product ')
    print('2- Edit product ')
    print('3- Search product ')
    print('4- Show List ')
    print('5- Qrcode ')
    print('6- Delete Product ')
    print('7- Buy Product ')
    print('8- Save information in Database')


showmenu()
choice = int(input('Please Choose a Number:'))
if choice == 1:
    ADD()
elif choice == 2:
    EDIT()
elif choice == 3:
    SEARCH()
elif choice == 4:
    show_list()
elif choice == 5:
    QRCODE()
elif choice == 6:
    DELETE()
elif choice == 7:
    BUY()
elif choice == 8:
    SAVE()
