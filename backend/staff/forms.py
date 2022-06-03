from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (

            'username',

            'staff_first_name',
            'staff_last_name',

            'staff_title',
            
            'staff_phone',
            'staff_email',

            )
    


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = (

            'username',

            'staff_first_name',
            'staff_last_name',

            'staff_title',
            
            'staff_phone',
            'staff_email',

            )