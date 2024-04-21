from django.shortcuts import render, get_object_or_404
from .models import Food



def food_list(request):
    """This view is related to the list of foods on the main page."""

    food_list = Food.objects.all()
    context = {
        "foods" : food_list
    }
    return render(request,"foods/list.html",context)
    
    

def food_detail(request , id):
    """This view is related to the details of the food."""

    food = get_object_or_404(Food, id = id)
    context = {
        "food":food
    }
    return render(request,"foods/detail.html",context)

