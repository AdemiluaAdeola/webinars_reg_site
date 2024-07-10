from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from user.forms import RegistrationForm
#from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # Load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=user.username, password=raw_password)
            auth.login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def login(response):
    if response.method == 'POST':
        username = response.POST['username']
        password = response.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(response, user)
            return redirect('/')
        else:
            messages.info(response, 'Credentials Invalid')
            return redirect('login')
    
    return render(response, 'registration/login.html')

@login_required(login_url='login')
def logout(response):
    auth.logout(response)
    return redirect('webinar_list')