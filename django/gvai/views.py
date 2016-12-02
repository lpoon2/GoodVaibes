from django.shortcuts import render
from gvai.models import Albums, Artists, Songs, Users
from rest_framework import viewsets
from gvai.serializers import AlbumSerializer, ArtistSerializer, SongSerializer
from django.views.generic import ListView
from django.core import serializers
from django.shortcuts import render_to_response  
import operator
from django.db.models import Q

from django.http import HttpResponse
from itertools import chain
# Create your views here.
def getRecommend(request):
    name = Users.objects.get(name='Larry').name.encode('ascii','ignore')
    history = Users.objects.get(name='Larry').favorite.encode('ascii','ignore')
    arr = history.split(',')
    dic = {x : arr.count(x) for x in arr}
    sort_arr = sorted(dic.items(), key=lambda x:x[1], reverse = True)
    arr1 = set(arr)
    queryset = Songs.objects.filter(Genre__icontains=arr[0])[:2];
    for i in range(1,len(sort_arr)):
        queryset = list(chain(queryset,Songs.objects.filter(Genre__icontains=arr[i])[:2]))
    #return Response(serializers.serialize('json', queryset)) 
    return render_to_response('test.html', { 'song_listing': queryset , 'name': name})

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
def BasicQuery(request):
	result = [{}]
	if request.GET.get('q') and '1' in request.GET:
		r = request.GET.get('q')
		result = Songs.objects.filter(Title__icontains=r) 
	return render_to_response('index.html',{ 'result' : result } )

def createItem(request):
	if request.method == "POST":
		#song = Songs(request.POST, instance = post)
		name = request.POST.get('name')
		genre = request.POST.get('genre')
		song = Songs(Title = name, Genre = genre) 
		song.save()
	return  render(request,'create.html', {'poll','asd'})

class BasicQuery2(ListView):
	template_name = 'gvai/index.html'
	queryset = Songs

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


