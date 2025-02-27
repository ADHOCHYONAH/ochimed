from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Omegameds
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .form import UserCreationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


def home(request):
    omegameds = Omegameds.objects.all()

    return render(request, 'home.html', {'omegameds': omegameds})


def shop(request):
    omegameds = Omegameds.objects.all()

    return render(request, 'shop.html', {'omegameds': omegameds})


def Read(request):
    omegameds = Omegameds.objects.all()

    return render(request, 'Read_more.html', {'omegameds': omegameds})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            htmly = get_template('email.html')
            d = {'username': username}
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'Register.html', {'form': form, 'title': 'register here'})


def Login(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('home')
        else:
            messages.info(request, f'account does not exist please sign in')
    form = AuthenticationForm()
    return render(request, 'Login.html', {'form': form, 'title': 'log in'})


def about(request):
    Read = Omegameds.objects.all()

    return render(request, 'About.html', {'Read': Read})


def contact(request):
    Contact = Omegameds.objects.all()
    return render(request, 'contact.html', {'Contact': Contact})
