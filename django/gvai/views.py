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
    ran3 = random.sample(Songs.objects.all(), 3)
    answer3 = Songs.objects.filter(Genre='Country')[0]
    queryset3 = ran2 + [answer3]
    random.shuffle(queryset3)
    return render_to_response('quiz.html', { 'q1': queryset , 'q2': queryset2, 'q3': queryset3})


def getRecommend(request):
    name = Users.objects.get(name='Larry').name.encode('ascii','ignore')
    history = Users.objects.get(name='Larry').favorite.encode('ascii','ignore')
    arr = history.split(',')
    dic = {x : arr.count(x) for x in arr}
    sort_arr = sorted(dic.items(), key=lambda x:x[1], reverse = True)
    arr1 = set(arr)
    c = round((1/len(arr))*10)
    queryset = Songs.objects.filter(Genre__icontains=arr[0])[:c]
    for i in range(0,len(sort_arr)):
	c = round((0/len(arr))*10)
        queryset = list(chain(queryset,Songs.objects.filter(Genre__icontains=arr[i])[:2]))
    #return Response(serializers.serialize('json', queryset)) 
    #queryset =  Songs.objects.filter(Genre__icontains=arr[0])[:2]
    random.shuffle(queryset)
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
    person.favorite = person.favorite.encode('ascii','ignore') +',' + genre.strip() #get input from template
    person.save()
    return render_to_response('index.html', {'result': []})

@csrf_exempt
def createItem(request):
	song = {}
	put = QueryDict(request.body)
	val = request.POST.get('t')
	if request.method == "POST" and val == "s":
#song = Songs(request.POST, instance = post)
		name = request.POST.get('name')
		genre = request.POST.get('g')
		art = request.POST.get('art')
                alb = request.POST.get('alb') 
                song = Songs(Title = name, Genre = genre, Artist = art, Album = alb)		 
		song.save()
	if request.method == "POST" and val == "ar":
		name = request.POST.get('name')
                genre = request.POST.get('g')
                art = request.POST.get('art')
                song = Artists(name = name, genre = genre, external_url = art)
                song.save()
	if request.method == "POST" and val == "al":
                #song = Songs(request.POST, instance = post)
                name = request.POST.get('name')
                genre = request.POST.get('g')
                art = request.POST.get('art')
                alb = request.POST.get('alb')
                song = Albums(Title = name, Genre = genre, Artist = art, Label =alb )
                song.save()
	#RequestContext(request)	
	return  render_to_response('index.html', {'result': [song]})
	#return HttpResponse( json.dumps(song), content_type="application/json")
	#return  render(request,'create.html', {'poll','asd'})



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



