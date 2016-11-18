from django.shortcuts import render
from gvai.models import Album, Artist, Song
from rest_framework import viewsets
from gvai.serializers import AlbumSerializer, ArtistSerializer, SongSerializer

# Create your views here.


class AlbumViewSet(viewsets.ModelViewSet):

	"""
	API endpoint that allows Albums to be viewed or edited.
	"""
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer

	class Meta:
		db_table = 'Album'


class ArtistViewSet(viewsets.ModelViewSet):

	"""
	API endpoint that allows Artists to be viewed or edited.
	"""

	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer

	class Meta:
		db_table = 'Artist'


class SongViewSet(viewsets.ModelViewSet):

	"""
	API endpoint that allows Songs to be viewed or edited.
	"""

	queryset = Song.objects.all()
	serializer_class = SongSerializer

	class Meta:
		db_table = 'Song'
