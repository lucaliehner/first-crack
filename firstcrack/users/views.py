from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
# Create your views here.

def authentication(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('home:index'))
        
        else:
            return redirect('sales:sales')

        

