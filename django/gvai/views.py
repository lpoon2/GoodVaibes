from django.shortcuts import render
from gvai.models import Albums, Artists, Songs
from rest_framework import viewsets
from gvai.serializers import AlbumSerializer, ArtistSerializer, SongSerializer

# Create your views here.


class AlbumViewSet(viewsets.ModelViewSet):

	"""
	API endpoint that allows Albums to be viewed or edited.
	"""
	queryset = Albums.objects.all()
	serializer_class = AlbumSerializer

	class Meta:
		db_table = 'Albums'


class ArtistViewSet(viewsets.ModelViewSet):

	"""
	API endpoint that allows Artists to be viewed or edited.
	"""

	queryset = Artists.objects.all()
	serializer_class = ArtistSerializer

	class Meta:
		db_table = 'Artists'


class SongViewSet(viewsets.ModelViewSet):

	"""
	API endpoint that allows Songs to be viewed or edited.
	"""

	queryset = Songs.objects.all()
	serializer_class = SongSerializer

	class Meta:
		db_table = 'Songs'


