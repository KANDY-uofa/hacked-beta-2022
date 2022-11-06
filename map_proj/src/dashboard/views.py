from django.shortcuts import render
import folium, geocoder
from folium import plugins
from .models import Data

def index(request):
    data = Data.objects.all()
    # returns the list of objects in list 
    data_list = Data.objects.values_list('latitude','longitude','reports_2022')
    map = folium.Map(location=[53.544389,-113.4909],zoom_start=5.5)
    plugins.HeatMap(data_list).add_to(map)
    plugins.Fullscreen(position = 'topright').add_to(map)
    map = map._repr_html_()
    context ={
        'map':map
    }
    return render(request, "dashboard/index.html",context)