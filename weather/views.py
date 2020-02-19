import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    # weather api
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1"

    err_msg = ""
    message = ""
    message_class = ""

    if request.method == "POST":
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data["name"]
            existing_city_count = City.objects.filter(name=new_city).count()

            # if city doesn't already exist than save it
            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()
                # cod 200 represents city existing
                if r["cod"] == 200:
                    form.save()
                else:
                    err_msg = "City does not exist in the world!"
            else:
                err_msg = "City Already Exist!"

    if err_msg:
        message = err_msg
        message_class = "is-danger"
    else:
        message = "City added successfully!"
        message_class = "is-success"

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        # display this form api
        city_weather = {
            "city": city.name,
            "temperature": r["main"]["temp"],
            "description": r["weather"][0]["description"],
            "icon": r["weather"][0]["icon"],
        }

        weather_data.append(city_weather)

    print(weather_data)

    context = {
        "weather_data": weather_data,
        "form": form,
        "message": message,
        "message_class": message_class,
    }
    return render(request, "weatherv2.html", context)


def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()
    return redirect("weather")

