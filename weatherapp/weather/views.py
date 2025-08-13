from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm

from json import load
from requests import get as req_get

with open('static/config.json', 'r') as f:
    config = load(f)

def weather_page(request):
    api_key = config['API_KEY']
    url = f'https://api.openweathermap.org/data/2.5/weather?q={{}}&units=metric&lang=ru&appid={api_key}'

    error_message = ''
    message = ''
    message_class = ''

    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()

            if existing_city_count == 0:
                r = req_get(url.format(new_city)).json()

                if r['cod'] == 200:
                    form.save()
                else:
                    error_message = f'Города "{new_city}" не существует!'
            else:
                error_message = f'Город "{new_city}" уже добавлен!'

        if error_message:
            message = error_message
            message_class = 'is-danger'
        else:
            message = f'Город "{new_city}" успешно добавлен'
            message_class = 'is-success'

    form = CityForm()

    cities = City.objects.all()
    weather_data = []

    for city in cities:
        r = req_get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {
        'weather_data': weather_data,
        'form': form,
        'message': message,
        'message_class': message_class
    }

    return render(request, 'weather/weather.html', context)

def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()

    return redirect('weather')
