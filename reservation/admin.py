from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class Reservationadmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "number", "date", "time")
