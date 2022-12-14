from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm #import the new form

def register(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') # get the username from the form submitted
            messages.success(request, f'Your account has been successfully created! You are now able to login.') #display a message after account created
            return redirect('login') #redirect to the desired page
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
