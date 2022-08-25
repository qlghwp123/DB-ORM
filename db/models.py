from django.db import models

class Director(models.Model):
    name = models.TextField()
    debut = models.DateTimeField()
    country = models.TextField()

    def print(self):
        print("id :", self.id)
        print("name :", self.name)
        print("debut :", self.debut)
        print("country :", self.country)

class Genre(models.Model):
    title = models.TextField()

    def print(self):
        print("id :", self.id)
        print("title :", self.title)

class Movie(models.Model):
    director = models.ForeignKey(Director,on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    title = models.TextField()
    opening_date = models.DateField()
    running_time = models.IntegerField()
    screening = models.BooleanField()

    def __init__(self):
        super()

    def __init__(self, _director, _genre, _title, _opening_date, _running_time, _screening):
        self.director = Director.objects.get(name=_director)
        self.genre = Genre.objects.get(title=_genre)
        self.title = _title
        self.opening_date = _opening_date
        self.running_time = _running_time
        self.screening = _screening

    def print(self):
        print(self.director, 
                self.genre, 
                self.title, 
                self.opening_date,
                self.screening
            )