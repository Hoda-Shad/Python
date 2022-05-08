from Media import Media


class Film(Media):
    def __init__(self, name, director, imdb_score, url, duration, cast):
        Media.__init__(self, name, director, imdb_score, url, duration, cast)

    def Edit_Film(self):
        choice = int(input('For edit the name press 1, for director press 2,for Imdb_Score press 3'
                           'for url press 4, for duration press 5, for cast press 6: '))
        if choice == 1:
            newname = input("enter new name: ")
            self.name = newname
            print('Editing is done successfully!')
        elif choice == 2:
            newdirector = input('Enter new director: ')
            self.director = newdirector
            print('Editing is done successfully!')
        elif choice == 3:
            newimdb = float(input('Enter new IMDBScore :'))
            self.imdb_score = newimdb
            print('Editing is done successfully!')
        elif choice == 4:
            newurl = input('Enter new URL: ')
            self.url = newurl
            print('Editing is done successfully!')
        elif choice == 5:
            newdur = int(input('Enter new duration :'))
            self.duration = newdur
            print('Editing is done successfully!')
        elif choice == 6:
            newcast = input('Enter the list of Casts: ')
            self.cast = newcast
            print('Editing is done successfully!')
        else:
            print('Input is not valid')

    def show_database(self):
        Media.Show_Info(self)

    def Download(self):
        link = input ('type/paste the link:')
        Media.Download(link)