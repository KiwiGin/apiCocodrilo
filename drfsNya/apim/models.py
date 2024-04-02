from django.db import models

# Models Roulette.
class Serie (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100)
    image_link = models.CharField(max_length=255)
    total_episodes = models.IntegerField()
    current_episode = models.IntegerField()
    current_season = models.IntegerField()
    status= models.CharField(max_length=100)
    
class Pelicula (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100)
    image_link = models.CharField(max_length=255)
    status= models.CharField(max_length=100)

class Anime (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100)
    image_link = models.CharField(max_length=255)
    total_episodes = models.IntegerField()
    current_episode = models.IntegerField()
    current_season = models.IntegerField()
    status= models.CharField(max_length=100)


