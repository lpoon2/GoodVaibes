from gvai.models import Album, Artist, Song
from rest_framework import serializers


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Album
		fields = ('num_tracks', 'genres', 'release_date', 'album_id', 'popularity', 'record_label', 'title')


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Artist
		fields = ('name', 'genre', 'external_url', 'artist_id')

class SongSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Song
		fields = ('title', 'song_id', 'genre', 'record_label', 'album', 'artist')