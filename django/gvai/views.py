from django.shortcuts import render
from gvai.models import Albums, Artists, Songs
from rest_framework import viewsets
from gvai.serializers import AlbumSerializer, ArtistSerializer, SongSerializer
from django.views.generic import ListView

import operator
from django.db.models import Q

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


class BasicQuery(ListView):
	"""
    Display an Album/Song/Artist List page filtered by the search query.
    """
	paginate_by = 10

	def get_queryset(self):
		result = super(BasicQuery, self).get_queryset()

		query = self.request.GET.get('q')
		if query:
			query_list = query.split()
			result = result.filter(
				reduce(operator.and_,
					(Q(album__icontains=q) for q in query_list)) |
				reduce(operator.and_,
					(Q(artist__icontains=q) for q in query_list)) |
				reduce(operator.and_,
					(Q(song__icontains=q) for q in query_list))
				)

		return result


