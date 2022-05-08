from series import Series
from clip import Clip
from film import Film
from documentory import Documentory
from Media import Media
from Actor import Actor


class main:
    def __init__(self):
        self.Item = []

    def read_data(self):
        f = open('database', 'r')
        line = f.read().split('\n')
        for i in range(len(line) - 1):
            info = line[i].split(',')

            if info[0] == 'Film':
                film = Film(info[1], info[2], info[3], info[4], int(info[5]), info[6])
                self.Item.append(film)

            elif info[0] == 'Series':
                series = Series(info[1], info[2], info[3], info[4], info[5], info[6], info[7])
                self.Item.append(series)

            elif info[0] == 'Documentary':
                documentory = Documentory(info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8])
                self.Item.append(documentory)

            elif info[0] == 'Clip':
                clip = Clip(info[1], info[2], info[3], info[4], info[5], info[6], info[7])
                self.Item.append(clip)

    def Add_Item(self):
        choice = int(input('For adding a Film press 1, Documentary press 2, Series press 3, Clip press 4'))
        name = input('Enter name: ')
        director = input('Enter Director')
        imdb_score = int(input('Enter the IMDB Score: '))
        url = input('Enter URL: ')
        duration = int(input('Enter the time: '))
        cast = input('Enter the list of Actress: ')

        if choice == 1:
            self.Item.append(Film(name, director, imdb_score, url, duration, cast))
            print('Adding was done successfully')

        elif choice == 2:
            numofepisods = int(input('Enter the number of episodes: '))
            sub = input('Enter the subject: ')
            self.Item.append(Documentory(name, director, imdb_score, url, duration, cast, numofepisods, sub))
            print('Adding was done successfully')

        elif choice == 3:
            numofepisods = int(input('Enter number of episodes:'))
            self.Item.append(Series(name, director, imdb_score, url, duration, cast, numofepisods))
            print('Adding was done successfully')

        elif choice == 4:
            subject = input('Enter the subject: ')
            self.Item.append(Clip(name, director, imdb_score, url, duration, cast, subject))
            print('Adding was done successfully')

    def Edit_Item(self):
        choice = int(input('For Editing thr Film press 1, Documentary press 2, Series press 3, Clip press 4: '))
        i = main.Search(self)
        if choice == 1:
            Film.Edit_Film(self.Item[i])
        elif choice == 2:
            Documentory.Edit_Documentory(self.Item[i])
        elif choice == 3:
            Series.Edit_Series(self.Item[i])
        elif choice == 4:
            Clip.Edit_Clip(self.Item[i])

    def Delete_Item(self):
        i = main.Search(self)
        if i is not None:
            del (self.Item[i])
            print('Deleting is done')

    def Search(self):
        flag = 1
        queryname = input('Enter the name? ')
        for i in range(len(self.Item)):
            if queryname == self.Item[i].name:
                print('Item found')
                flag = 0
                return i
        if flag == 1:
            print("Item not found")

    def Show_Item(self):
        for i in range(len(self.Item)):
            print(self.Item[i].show_database())

    def Advanced_Search(self):
        flag = 0
        f_digit = int(input('Enter the first time:'))
        s_digit = int(input('Enter the second time'))
        for i in range(len(self.Item)):
            if f_digit < self.Item[i].duration < s_digit:
                print(self.Item[i].show_database())
                flag = 1
        if flag == 0:
            print('Item not found')

    def Save_Item(self):
        f = open('database', 'w')
        for i in self.Item:
            if type(i).__name__ == 'Film':
                row = 'film' + ',' + i.name + ',' + i.director + ',' + str(i.imdb_score) + ',' + i.url + ',' + str(
                    i.duration) + ',' + i.cast + '\n'
                f.write(row)
            elif type(i).__name__ == 'Documentory':
                row = 'documentory' + ',' + i.name + ',' + i.director + ',' + str(
                    i.imdb_score) + ',' + i.url + ',' + str(
                    i.duration) + ',' + str(i.nepisods) + ',' + i.subject + '\n'
                f.write(row)
            elif type(i).__name__ == 'Series':
                row = 'series' + ',' + i.name + ',' + i.director + ',' + str(i.imdb_score) + ',' + i.url + ',' + str(
                    i.duration) + ',' + i.cast + ',' + str(i.numofepisodes) + '\n'
                f.write(row)
            elif type(i).__name__ == 'Clip':
                row = 'film' + ',' + i.name + ',' + i.director + ',' + str(i.imdb_score) + ',' + i.url + ',' + str(
                    i.duration) + ',' + i.cast + ',' + i.subject + '\n'
                f.write(row)
        print('You save the file successfully')
        f.close()

    def menu(self):
        while True:
            choice = int(input('Enter your choice:1 for Adding, 2 for Searching,3 for Advance Search, 4 for Deleting, '
                               '\n''\t''\t''\t''\t'' '' ''5 for Editing, ''6 for Showing, 7 for Saving, 8 for '
                               'Download or ''\n''\t''\t''\t''\t'' ' ' for exit '
                               'press 0:  '))
            if choice == 0:
                exit()
            elif choice == 1:
                self.Add_Item()
            elif choice == 2:
                self.Search()
            elif choice == 3:
                self.Advanced_Search()
            elif choice == 4:
                self.Delete_Item()
            elif choice == 5:
                self.Edit_Item()
            elif choice == 6:
                self.Show_Item()
            elif choice == 7:
                self.Save_Item()
            elif choice == 8:
                Media.Download(self)
            else:
                print('Invalid input')


a = main()
a.read_data()
a.menu()
