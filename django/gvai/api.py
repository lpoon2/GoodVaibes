from import_export import resources
from gvai.models import Song
class SongResource(resources.ModelResource):
	class Meta:
		queryset = Song.objects.all()
         	resource_name = 'song'
         	allowed_methods = ['post', 'get', 'patch', 'delete']
         #	authentication = Authentication()
         #	authorization = Authorization()
         	always_return_data = True
