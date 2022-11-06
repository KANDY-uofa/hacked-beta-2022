from django.contrib import admin
from .models import Data


class DataAdmin(admin.ModelAdmin):
    list_display = ('location', 'collisions', 'latitude', 'longitude')

# Register your models here.
admin.site.register(Data, DataAdmin)