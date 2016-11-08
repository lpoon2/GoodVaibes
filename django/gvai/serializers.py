from rest_framework import serializers
from gvai.models import Song 

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title', 'song_id', 'genre', 'record_label')



