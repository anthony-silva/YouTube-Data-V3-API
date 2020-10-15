from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import LoginForm, RegisterForm

User = get_user_model()

def LoginView(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect("/")
        else:
            request.session['invalid_user'] = 1 # 1 == True
    template = 'login.html'
    return render(request, template, {'form': form})


def LogoutView(request):
    logout(request)
    return redirect('/')


def RegisterView(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        try:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
        except:
            user = None
        if user != None:
            login(request, user)
            return redirect('/')
        else:
            request.session['register_error'] = 1

    template = 'register.html'
    return render(request, template, {'form': form})