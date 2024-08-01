from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login

from Checkpoint.forms import CustomLoginForm

from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'Checkpoint/login.html'  # Replace with your actual template path


#def LoginView(request):
   #return render(request, 'App/login.html')


def LoginView(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Checkpoint/userdashboard.html')  # Redirect to a success page.
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = CustomLoginForm()
    return render(request, 'App/login.html', {'form': form})