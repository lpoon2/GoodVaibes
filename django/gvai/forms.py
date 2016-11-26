from django.forms import ModelForm
from gvai.models import Albums, Artists, Songs
import cgi

# To Do: Make sure this works, or use jquery/ajax calls

form = cgi.FieldStorage()
searchterm =  form.getvalue('query')

Albums.objects.raw(SELECT * FROM Album WHERE title = %s, searchterm)
Artists.objects.raw(SELECT * FROM Artists WHERE title = %s, searchterm)
Songs.objects.raw(SELECT * FROM Songs WHERE title = %s, searchterm)

