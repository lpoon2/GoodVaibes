"""_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from gvai import views
from django.views.generic import TemplateView
#from spotify import views

router = routers.DefaultRouter()
router.register('albums', views.AlbumViewSet)
router.register('artists', views.ArtistViewSet)
router.register('songs', views.SongViewSet)
#router.register('search', views.BasicQuery, base_name = 'search')

# Wire up API using automatic URL routing, include login URLS for the browsable API

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    #url(r'^search', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^search', views.BasicQuery, base_name = 'search'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    #url(r'^insights/')
]
