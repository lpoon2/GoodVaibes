from gvai.models import Albums, Artists, Songs
from rest_framework import serializers


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Albums
		fields = ('title', 'genre', 'album_id', 'artist', 'label', 'length')


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Artists
		fields = ('name', 'genre', 'external_url', 'artist_id')

class SongSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Songs
		fields = ('title', 'song_id', 'genre', 'record_label', 'album', 'artist')
