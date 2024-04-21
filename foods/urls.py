from django.urls import path
from . import views


app_name = "foods"
urlpatterns = [
    path("", views.food_list, name="food_names"),
    path("<int:id>/", views.food_detail, name="detail"),
]
