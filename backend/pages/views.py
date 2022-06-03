from django.shortcuts import render

# from premise.models import Ardhi


def home_view(request):
    # posts = Ardhi.objects.all()[0:1]
    # context = {
    #     "posts": posts,
    # }
    return render(request, "pages/home.html")