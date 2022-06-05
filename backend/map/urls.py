from django.urls import path

from . import views
from .views import AddPlaceView #ChangePlaceView, PlacesView

urlpatterns = [

    #path("add-new/", views.add_vehicle, name="add_facility"),
    path("view-all/", views.all_facilities, name="all_facilities"),

    path("add-new/", AddPlaceView.as_view(), name="add_facility"),

]