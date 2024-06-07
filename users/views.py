from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form =  UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created successfully. Pls Login to proceed')
            return redirect('login')
    else:
        form =  UserRegisterForm()
    return render(request, 'users/register.html', 
                  {'form' : form})

def logout_view(request):
    messages.info(request, "Logged Out Successfully")
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'users/profile.html')