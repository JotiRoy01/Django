
from django.urls import path
from . import views

# localhost:8000/my_firstApp
# localhost:8000/myfirstApp/order
urlpatterns = [
    path("", views.my_firstApp, name="my_firstApp"),
    #path("", views.order, name="order"),

]