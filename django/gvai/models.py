from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Albums(models.Model):
    title = models.CharField(max_length=50)
    genre = models.TextField()
    album_id = models.IntegerField(primary_key=True)
    artist = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    length = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Albums'


class Artists(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    external_url = models.CharField(max_length=50, blank=True)
    artist_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Artists'


class Songs(models.Model):
    title = models.CharField(max_length=50)
    song_id = models.IntegerField(primary_key=True)
    genre = models.CharField(max_length=50)
    record_label = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Songs'

class Users(models.Model):
    name = models.CharField(max_length=20)
    favorite = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Users'
