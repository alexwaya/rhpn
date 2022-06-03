from django.urls import path

from . import views

urlpatterns = [

    #path("add-new/", views.add_vehicle, name="add_facility"),
    path("view-all/", views.all_facilities, name="all_facilities"),

]