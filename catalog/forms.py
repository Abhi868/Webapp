
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    model=CustomUser
    fields=("email","username")

class CustomUserChangeForm(UserChangeForm):
    model=CustomUser
    
