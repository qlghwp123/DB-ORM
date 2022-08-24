from django.db import models

class Director(models.Model):
    name = models.TextField()
    debut = models.DateTimeField(null=True)
    country = models.TextField()

    def print(self):
        print(self.name, self.debut, self.country)

class Genre(models.Model):
    title = models.TextField(null=True)