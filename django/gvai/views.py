from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from gvai.models import Song
from rest_framework import viewsets
from gvai.serializers import SongSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
def index(request):
    return HttpResponse("<h1>Hello, world !</h1>")

class SongViewSet(APIView):
	def get(self, request, format=None):
		queryset = Song.objects.all()
		serializer = SongSerializer(queryset, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = SongSerializer(data=request.data)
  		if serializer.is_valid():
            		serializer.save()
            		return Response(serializer.data, status=status.HTTP_201_CREATED)
        	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
# Create your views here.
