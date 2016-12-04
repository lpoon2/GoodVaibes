from django.shortcuts import render
from gvai.models import Albums, Artists, Songs, Users
from rest_framework import viewsets
from gvai.serializers import AlbumSerializer, ArtistSerializer, SongSerializer
from django.views.generic import ListView
from django.core import serializers
from django.shortcuts import render_to_response  
import operator
from django.http import QueryDict
from django.db.models import Q
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template import RequestContext
from django.http import HttpResponse
from itertools import chain
from rest_framework.decorators import detail_route
import random
import json
def getRandomAnswers(request):
    # which singer sang the following song Take a Back Road
    ran = random.sample(Songs.objects.all(), 3)
    answer = Songs.objects.filter(Title='Take a Back Road')[0]
    queryset = ran + [answer]
    random.shuffle(queryset)
    #which of the song is sang by Drake
    ran2 = random.sample(Songs.objects.all(), 3)
    answer2 = Songs.objects.filter(Artist='Drake')[0]
    queryset2 = ran2 + [answer2]
    random.shuffle(queryset2)
    return render_to_response('quiz.html', { 'q1': queryset , 'q2': queryset2})


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
	@detail_route(methods=['post'])
	def createItem(self, request, pk=None):
                s = SongSerializer(data=request.data)
                name = request.POST.get('name')
                genre = request.POST.get('genre')
                song = Songs(Title = name, Genre = genre)
                song.save()
		s.save()
        	return  Response(s.data, status=status.HTTP_201_CREATED)

	class Meta:
		db_table = 'Songs'

def BasicQuery(request):
	result = [{}]
	if request.GET.get('q') and '1' in request.GET:
		r = request.GET.get('q')
		result = Songs.objects.filter(Title__icontains=r) 
	return render_to_response('index.html',{ 'result' : result } )

#@csrf_protect
@csrf_exempt
def update_history(request):
    person = Users.objects.get(name='Larry')  #request.GET.get('genre')
    put = QueryDict(request.body)
    genre = put.get('genre')
    person.favorite = person.favorite.encode('ascii','ignore') +',' + genre #get input from template
    person.save()
    return render_to_response('index.html', {'result': []})

@csrf_exempt
def createItem(request):
	song = {}
	if request.method == "POST":
		#song = Songs(request.POST, instance = post)
		name = request.POST.get('name')
		genre = request.POST.get('genre')
		song = Songs(Title = name, Genre = genre) 
		song.save()
	#RequestContext(request)	
	return  render_to_response('index.html', {'result': [song]}  )
	#return HttpResponse( json.dumps(song), content_type="application/json")
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


