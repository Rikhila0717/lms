from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpRequest
from app_users.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

#home page
def index(request):
    return render(request,'home.html')


#user register page
def register(request):

    registered = False
    #POST is when the user clicks the submit button

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            #save the user form
            user = user_form.save()
            user.save()

            #Link the profile and the user

            profile = profile_form.save(commit=False)
            profile.user=user
            profile.save()

            #user is registered successfully
            registered=True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        #if the user is not posting anything, render out the blank forms
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context = {
        'registered': registered,
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'app_users/registration.html',context)

#userlogin page
def user_login(request):

    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:

            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT IS DEACTIVATED")

        else:
            return HttpResponse("Please use correct user-id and password")

    else:
        return render(request,'app_users/login.html')

    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))




