from django.db import models

# Create your models here.

# tunr/models.py
class Artist(models.Model):
    # models comes from line 1 - DJANGODB
    name = models.CharField(max_length=100)
    current_country = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name

# make sure to add migrations when you change things in database
# to check database run 'psql tunr' then '\c tunr'

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
# on_delete.CASCADE will delete artist and any song related to it
    title = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    preview_url = models.TextField()

    def __str__(self):
        return self.title