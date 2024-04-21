from django.contrib import admin
from .models import Food


@admin.register(Food)
class Foodadmin(admin.ModelAdmin):
    list_display = ('name', 'rate', 'price', 'time', 'pub_date')
    list_filter = ('rate', 'pub_date')
