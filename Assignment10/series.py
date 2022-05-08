from Media import Media


class Series(Media):
    def __init__(self, name, director, imdb_score, url, duration, cast, numofepisods):
        Media.__init__(self, name, director, imdb_score, url, duration, cast)
        self.nepisods = numofepisods

    def Edit_Series(self):
        choice = input('For edit the name press 1, for director press 2,for Imdb_Score press 3'
                       'for url press 4, for duration press 5, for cast press 6, 7 for number of episodes')
        if choice == 1:
            newname = input("enter new name: ")
            self.name = newname
        elif choice == 2:
            newdirector = input('Enter new director: ')
            self.director = newdirector
        elif choice == 3:
            newimdb = float(input('Enter new IMDBScore :'))
            self.imdb_score = newimdb
        elif choice == 4:
            newurl = input('Enter new URL: ')
            self.url = newurl
        elif choice == 5:
            newdur = int(input('Enter new duration :'))
            self.duration = newdur
        elif choice == 6:
            newcast = input('Enter the list of Casts: ')
            self.cast = newcast
        elif choice == 7:
            newnum = int(input('Enter the new number of Episods: '))
            self.nepisods = newnum
        else:
            print('Input is not valid')


    def show_database(self):
        Media.Show_Info(self)
        print ('Number of episodes:', self.nepisods)
