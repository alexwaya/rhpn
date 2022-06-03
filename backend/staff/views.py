from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# @login_required
# def add_staff(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
            
#             return redirect('all_staff')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'staff/add_staff.html', {'form': form})

# @login_required
# def all_staff(request):
# 	posts = CustomUser.objects.all()[1:]
# 	context = {
# 		"posts": posts,
#     }
# 	return render(request, "staff/all_staff.html", context)