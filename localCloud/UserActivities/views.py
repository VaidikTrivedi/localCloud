from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from .form import CreateUserForm
from . import models

# Create your views here.
def home(request):
    return render(request, 'webpages/home.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print(user)
        #print(user.is_authenticated)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Login Credentials Wrong! Please try again')
            return redirect('login')

    return render(request, 'webpages/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            fname = form.cleaned_data.get('first_name')
            lname = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            dob = form.cleaned_data.get('date_of_birth')
            # gender = form.cleaned_data.get('gender_identity')
            form.save()
            models.User(fname, lname, dob, username=username, email=email)
            # user.save()
            valid_user = authenticate(request, username=username, password=password)
            print("\n\nValid User: ", valid_user)
            #print("\n\n", username, password, user, "IF STARTTING \n\n")
            if valid_user is not None:
                login(request, valid_user)
                # print("User Id: ", request.user.id)
                # student = get_user_model().objects.get(id=request.user.id)
                # group = Group.objects.get(name='grp_student')
                # group.user_set.add(student)
                messages.success(request, 'Registration Success as student!')
                return redirect('login')
            else:
                return redirect('register')

    context = {'form': form}
    return render(request, 'webpages/register.html', context)