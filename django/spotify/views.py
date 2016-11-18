from django.shortcuts import render
import base64
import urllib2

# Create your views here

@staticmethod
def loginCallback(request_handler, code):
    url = 'https://accounts.spotify.com/api/token'
    authorization = base64.standard_b64encode('7b6a8408eb3542b290236610a2cbfe2f' + ':' + '187908062662472cb11ee6031e7fb282')
    # format is client_id:secret_id

    headers = {
        'Authorization' : 'Basic ' + authorization
        } 
    data  = {
        'grant_type' : 'authorization_code',
        'code' : code,
        'redirect_uri' : Spotify.redirect_uri
        } 

    data_encoded = urllib.urlencode(data)
    req = urllib2.Request(url, data_encoded, headers)

    try:
        response = urllib2.urlopen(req, timeout=30).read()
        response_dict = json.loads(response)
        Spotify.saveLoginCallback(request_handler, response_dict)
        return
    except urllib2.HTTPError as e:
        return e
