from django.urls import path
from .views import SignUpView

from . import views

urlpatterns = [

    path('signup/', SignUpView.as_view(), name='signup'),

    # path("new/", views.add_staff, name="add_staff"),
    # path("all/", views.all_staff, name="all_staff"),

]