from django.http import HttpResponse, HttpResponseRedirect
from .forms import UpdateProfileBillingForm, UpdateProfileForm, UpdateUserForm, UserRegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import User


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/registration-success')
        else: 
            return HttpResponse('Form not valid!')
    
    else:
        form = UserRegistrationForm()
        return ('User cannot be created')


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                # return HttpResponse("User successfully logged in!")
                return HttpResponseRedirect('/user')
            else:
                return HttpResponse("Login unsuccessful!")
        else:
            return HttpResponse("Invalid email or password")

    form = AuthenticationForm()    


def logoutUser(request):
   logout(request)
   return HttpResponseRedirect('/')


def update_user(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user_form = UpdateUserForm(request.POST, instance=request.user)
            profile_form = UpdateProfileForm(request.POST, instance=request.user.profile)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                return HttpResponseRedirect('/user')
            else:
                print(profile_form)
                return HttpResponse('Error!')
    else:
        return HttpResponseRedirect('/login')

def update_billing(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            profile_form = UpdateProfileBillingForm(request.POST, instance=request.user.profile)
            if profile_form.is_valid():
                profile_form.save()
                return HttpResponseRedirect('/user')
            else:
                print(profile_form)
                return HttpResponse('Error!')
    else:
        return HttpResponseRedirect('/login')