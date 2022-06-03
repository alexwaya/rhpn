from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import FacilityForm

from .models import Facility
from staff.models import CustomUser


@login_required
def all_facilities(request):
	posts = Facility.objects.all()
	context = {
		"posts": posts,
    }
	return render(request, "map/all_facilities.html", context)


# @login_required
# def add_facilities(request):
# 	posts = CustomUser.objects.all()[1:]

# 	if request.method == 'POST':
# 		form = VehicleForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			form.save()
            
# 			return redirect('all_vehicles')
# 	else:
# 		form = VehicleForm()

# 	context = {
# 		"posts": posts,
# 		"form": form,
#     }
# 	return render(request, 'map/add_facilities.html', context)


