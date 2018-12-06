# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from user_app.forms import UserForm, UserProfileInfoForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# from django.urls import reverse


# Create your views here.
def base(request):
    return render(request, 'user_app/base.html')


def index(request):
    return render(request, 'user_app/index.html')


def registration(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()  # one to one relation

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

                profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'user_app/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("SOme one try to login")
            print("Username: {} Password: {}".format(username, password))
            return HttpResponse("Invalid Login Details Supplied!")
    else:
        return render(request, "user_app/login.html", {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    return HttpResponse("your logged in, Nice !")
