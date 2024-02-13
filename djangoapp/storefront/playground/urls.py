from django.urls import path
from . import views

#URL_configuration_module
urlpatterns = [
    path('hello/',views.say_hello)
]