from django.shortcuts import render, redirect
from django.urls import reverse
from mainapp.forms import MediaFileForm, RegisterUserForm, UserLoginForm
from django.contrib.auth.models import User
from mainapp.models import MediaFile
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages



def user_register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainapp:login')
    else:
        form = RegisterUserForm()
    return render(request, 'user/register.html', {'form':form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)
                messages.success(request,'successfully logged in')
                return redirect(reverse('mainapp:upload_file'))
            else:
                messages.error(request, 'Invalid username / password!')
        else:
            messages.error(request, 'Invalid! username / password')
    
    form = UserLoginForm()    
    return render(request, 'user/login.html', {'form':form})


def user_logout(request):
    logout(request)
    return redirect('mainapp:upload_file')


def upload_file(request):
    form = MediaFileForm()

    if request.method == 'POST':
        form = MediaFileForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            if request.user.is_authenticated:
                mediafile = form.save(commit=False)
                mediafile.user = request.user  # Assign the logged-in user
                mediafile.save()
                return redirect(reverse('mainapp:file_list'))
            else:
                messages.error(request, 'You are not a user. Please log in.')

    return render(request, 'media_app/upload.html', {'form': form})



def file_list(request):
    files = MediaFile.objects.all()
    return render(request, 'media_app/file_list.html', {'files':files})


