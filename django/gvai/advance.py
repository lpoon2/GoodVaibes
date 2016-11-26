from itertools import chain
from rest_framework.response import Response
from django.core import serializers
def getRecommend(request):
    history = Users.objects.get(name='abc').favorite.encode('ascii','ignore')
    arr = history.split(',')
    dic = {x : arr.count(x) for x in arr}
    sort_arr = sorted(dic.items(), key=lambda x:x[1], reverse = True)
    arr1 = set(arr)
    queryset = Songs.objects.get(genre__icontains=arr1[i])[:sort_arr[arr1[0]]];
    for i in range(1,len(sort_arr)):
        queryset = list(chain(queryset,Songs.objects.get(genre__icontains=arr1[i])[:sort_arr[arr1[i]]]))
    return Response(serializers.serialize('json', queryset))

def update_history(request):
    person = Users.objects.get(nam='abc')
    person.history = person.history + ','+ request.PUT.get('input') #get input from template
    person.save()
    return Response(serializers.serialize('json', person))
