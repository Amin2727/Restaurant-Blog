from django.shortcuts import render, redirect
from django.views import View
from .forms import ReservationForm


def reserve(request):
    """This view is related to making a reservation in a restaurant."""
    
    reserve_form = ReservationForm()
    if request.method == "POST":
        reserve_form = ReservationForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
    else:
        reserve_form = ReservationForm()

    context = {
        "form":reserve_form,
    }

    return render(request,"reservation/reservation.html",context)