from Media import Media


class Clip(Media):
    def __init__(self, name, director, imdb_score, url, duration, cast, subject):
        Media.__init__(self, name, director, imdb_score, url, duration, cast)
        self.subject = subject

    def Edit_Clip(self):
        choice = input('For Editing the name press1 , 2 for director, 3 for url,4 for duration, 5 for subject')
        if choice == 1:
            newname = input('Enter new name: ')
            self.name = newname
        elif choice == 2:
            newdirector = input('Enter new director: ')
            self.director = newdirector
        elif choice == 3:
            newurl = input('Enter new url: ')
            self.url = newurl
        elif choice == 4:
            newduration = int(input('enter new duration: '))
            self.duration = newduration
        elif choice == 5:
            newsubject = input('Enter new subject: ')
            self.subject = newsubject
        else:
            print('Input is not valid')

    def show_database(self):
       Media.Show_Info(self)
       print('Subject:', self.subject)