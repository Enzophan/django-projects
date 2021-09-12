from django.shortcuts import render
import json
import urllib.request
from urllib.parse import quote
# Create your views here.


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/weather?q=' + quote(city) + '&appid=dee87c3d50b0b887c864405a1e1a45ed').read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ', ' + str(json_data['coord']['lat']),
            "temp": str(float(json_data['main']['temp']) - 273.15) + ' Celsius',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']) + ' %',
        }
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})
