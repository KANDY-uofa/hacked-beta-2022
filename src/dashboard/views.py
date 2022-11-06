from django.shortcuts import render
import folium, geocoder
from folium import plugins
from .models import Data
from django.http import Http404


def sum(request):
    print("im sum")
    data_list = Data.objects.values_list('latitude','longitude','sum')
    map = folium.Map(location=[53.544389,-113.4909],zoom_start=6)
    plugins.HeatMap(data_list).add_to(map)
    plugins.Fullscreen(position = 'topright').add_to(map)
    map = map._repr_html_()
    context ={
    'map':map
    }
    return render(request, "dashboard/index.html", context)

def report_2022(request):
    print("im 2022")
    data_list = Data.objects.values_list('latitude','longitude','reports_2022')
    map = folium.Map(location=[53.544389,-113.4909],zoom_start=6)
    plugins.HeatMap(data_list).add_to(map)
    plugins.Fullscreen(position = 'topright').add_to(map)
    map = map._repr_html_()
    context ={
    'map':map
    }
    return render(request, "dashboard/2022.html", context)

def report_2021(request):
    print("im 2021")
    data_list = Data.objects.values_list('latitude','longitude','reports_2021')
    map = folium.Map(location=[53.544389,-113.4909],zoom_start=6)
    plugins.HeatMap(data_list).add_to(map)
    plugins.Fullscreen(position = 'topright').add_to(map)
    map = map._repr_html_()
    context ={
    'map':map
    }
    return render(request, "dashboard/2021.html", context)
