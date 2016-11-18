from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Albums(models.Model):
    num_tracks = models.IntegerField()
    genres = models.TextField()
    release_date = models.TextField()
    album_id = models.IntegerField(primary_key=True)
    popularity = models.IntegerField()
    record_label = models.TextField()
    title = models.TextField()

    class Meta:
        managed = False
        db_table = 'Albums'


class Artists(models.Model):
    name = models.CharField(max_length=11)
    genre = models.CharField(max_length=11)
    external_url = models.CharField(max_length=11)
    artist_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Artists'


class Songs(models.Model):
    title = models.CharField(max_length=11)
    song_id = models.IntegerField(primary_key=True)
    genre = models.CharField(max_length=11)
    record_label = models.CharField(max_length=11)
    album = models.CharField(max_length=11)
    artist = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'Songs'
