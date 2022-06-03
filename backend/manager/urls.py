from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.admin_index, name="admin_index"),

]