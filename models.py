from django.db import models

class Releases(models.Model):
    artist = models.CharField(max_length=200)
    release_name = models.CharField(max_length=100)
    bpm = models.CharField(max_length=160)
    release_date = models.CharField(max_length=175)
    download_link = models.CharField(max_length=500)
    class Meta:
        pass

class Members(models.Model):
    artist_name = models.CharField(max_length=200)
    artist_genre = models.CharField(max_length=200)
    class Meta:
        pass


