from django.forms import ModelForm
from gvai.models import Albums, Artists, Songs
import cgi

form = cgi.FieldStorage()
searchterm =  form.getvalue('query')

Albums.objects.raw(SELECT * FROM Album WHERE title = %s, searchterm)
Artists.objects.raw(SELECT * FROM Album WHERE title = %s, searchterm)
Songs.objects.raw(SELECT * FROM Album WHERE title = %s, searchterm)

