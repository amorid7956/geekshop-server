from django.shortcuts import render, HttpResponseRedirect
from .forms import UserLoginForm
from django.contrib import auth
from django.urls import reverse

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = { 'title' : 'GeekShop - Авторизация', 'form' : form }
    return render(request, 'authapp/login.html', context)

