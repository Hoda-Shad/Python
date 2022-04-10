import os.path
if os.path.isfile('database'):
    pass
else:
    print ("File is not exist")
words = []
f = open ('database' , 'r')

data = f.read()
data_list = data.split('\n')
for i in range (len(data_list)-1):
    word_info = data_list[i].split(',')

    worddict = {'english': word_info[0], 'persian': word_info[1]}

    words.append(worddict)
# print('words is list of: ', words)


def add_new():
    a = input('enter word in english:')
    b = input('enter word in persian:')
    newdict = { 'english' : a , 'persian' : b}
    words.append(newdict)
    print('The entire word added successfully')
    # print(words)

def translation_english_persian():
    total = ''
    # str(total)
    # print(type(total))
    list = []
    a = input('enter a world or sentence in english:')
    # while True:
    if '.' in a:
        sentence = a.split('.')
        for i in range(len(sentence)):
            list1 = sentence[i].split(' ')
            list.append(list1)
            flag = 1
        for j in range(len(list)):
            for l in range(len(list[j])):
                for k in range(len(words)):
                    if list[j][l] == words[k]['english']:
                        total = total + ' ' + (words[k]['persian'])
                        flag = 0
                if flag == 1:
                    total = total + ' ' + list[j][l]
            total = total + '.'
        print(total)
    else:
        list = a.split(' ')
        for i in range(len(list)):
            for k in range(len(words)):
                if list[i] == words[k]['english']:
                    total = total + ' ' + (words[k]['persian'])
                    flag = 0
            if flag == 1:
                total = total + ' ' + list[i]
        total = total + '.'
        print(total)

def translation_persian_english():
    total = ''
    # str(total)
    # print(type(total))
    list = []
    a = input('enter a world or sentence in Persian:')
    # while True:
    if '.' in a:
        sentence = a.split('.')
        for i in range(len(sentence)):
            list1 = sentence[i].split(' ')
            list.append(list1)
            flag = 1
        for j in range(len(list)):
            for l in range(len(list[j])):
                for k in range(len(words)):
                    if list[j][l] == words[k]['persian']:
                        total = total + ' ' + (words[k]['english'])
                        flag = 0
                if flag == 1:
                    total = total + ' ' + list[j][l]
            total = total + '.'
        print(total)
    else:
        list = a.split(' ')
        for i in range(len(list)):
            for k in range(len(words)):
                if list[i] == words[k]['persian']:
                    total = total + ' ' + (words[k]['english'])
                    flag = 0
            if flag == 1:
                total = total + ' ' + list[i]
        total = total + '.'
        print(total)

def exit_translation():
    f = open('database', 'w')
    for i in range(len(words)):
        row = words[i]['english'] + ',' + words[i]['persian'] + '\n'
        f.write(row)
    f.close()
    exit()

while True:
    def show_menu():
        print('1- add new word ')
        print('2- Translation English to persian')
        print('3- Translation persian to english')
        print('4- exit')
        choice = int(input('Enter you choice: '))
        if choice == 1:
            add_new()
        elif choice == 2:
            translation_english_persian()
        elif choice == 3:
            translation_persian_english()
        elif choice == 4:
            exit_translation()

    show_menu()
