import pytube
class Media():
    def __init__(self, name, director, imdb_score, url, duration, cast):
        self.name = name
        self.director = director
        self.imdb_score = imdb_score
        self.url = url
        self.duration = duration
        self.cast = cast

    def Show_Info(self):
        print('Name:', self.name, '\n', 'Director:', self.director, '\n', 'IMDB_Score:', self.imdb_score, '\n', 'URL:',
              self.url, '\n', 'Duration:', self.duration, '\n', 'Cast:', self.cast)

    def Download(self):
        link = input('Enter URL for downloading: ')
        first_stream = pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./', filename='test.mp4')
        print('Download is completed')


