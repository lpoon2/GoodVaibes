from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from gvai.models import Song
from django.http import JsonResponse
from rest_framework import viewsets
from gvai.serializers import SongSerializer
from django.http import Http404
from django.views import View
from django.core import serializers
import json
def index(request):
    return render(request, "main.html") 

class SongViewSet(View):
	def get(self, request, format=None):
		queryset = Song.objects.all()
		serializer = SongSerializer(queryset, many=True)
		return HttpResponse(serializers.serialize('json',queryset), content_type="application/json")

	def post(self, request, format=None):
		#serializer = SongSerializer(data=request.data)
  		#if serializer.is_valid():
            	#	serializer.save()
		try:
			dict = json.loads(request.body.decode("utf-8"))
		except:
			return JsonResponse({"status": "fail", "message": "Invalid request"})        
    	
		new_obj = Song.objects.create(genre=dict["genre"], title=dict["title"], record_label=dict["record_label"]
)
		new_obj.save() 

		return HttpResponse({"status": "okay", "id": new_obj.id}, status=status.HTTP_201_CREATED)
        	#return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	

# Create your views here.
