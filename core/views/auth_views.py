from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from core.models import Task,Activity,Staff
from core.forms import TaskForm,CreateUserForm,StaffForm
#from .filters import Taskfilter
#from .decorators import unauthenticated_user, allow_users , admin_only

def home(request):
    """
    Render the home page.
    """
    return render(request, 'core/index.html')

def registerPage(request):

    form= CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')


            messages.success(request, 'Account has been created ' + username)
            return redirect('login')

    context = {'form':form}
    return render(request, 'core/register.html', context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password= password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid email or Password")
    return render(request, 'core/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')


