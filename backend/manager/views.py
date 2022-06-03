from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required
def admin_index(request):
    # posts = Ardhi.objects.all().order_by('-created_on')
    # context = {
    #     "posts": posts,
    # }
    return render(request, "manager/admin_home.html")

