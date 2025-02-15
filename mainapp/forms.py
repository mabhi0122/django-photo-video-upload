from django import forms
from django.contrib.auth.models import User
from .models import MediaFile
from .validators import validate_file_size, validate_file_extensions
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class MediaFileForm(forms.ModelForm):
    file = forms.FileField(validators=[validate_file_size, validate_file_extensions])
    class Meta:
        model = MediaFile
        fields = ['title', 'media_type', 'file']


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']