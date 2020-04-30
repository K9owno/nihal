from django.shortcuts import render,redirect
from .import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Todo
from django.contrib.auth.models import User

# Create your views here.
todos = Todo.objects.all()
form = forms.todo()


def showtodo(request):
        return render(request,'showtodo.html',{'todos':todos})

def signup_view(request):
        if request.method == 'POST':
                signup_form = UserCreationForm(data=request.POST)
                if signup_form.is_valid():
                        signup_form.save()
                        # user = signup_form.get_user()
                        # login(request, user)
                        return redirect('/')
                else:
                        return render(request, 'Signup.html', {'form': signup_form})
        else:
                signup_form = UserCreationForm()
                return render(request,'Signup.html',{'form': signup_form})

def Login_view(request):
        if request.method == 'POST':
                Login_form = AuthenticationForm(data=request.POST)
                if Login_form.is_valid():
                        user = Login_form.get_user()
                        login(request, user)
                        return redirect('/')
                else:
                        return render(request, 'UserLogin.html', {'form': Login_form})
        else:
                Login_form = AuthenticationForm()
                return render(request,'UserLogin.html',{'form':Login_form})

def Logout_view(request):
        if request.method == 'POST':
                logout(request)
                return redirect('/')

@login_required(login_url="/Login/")
def createtodo(request):
        if request.method == 'POST':
                form = forms.todo(request.POST,request.FILES)
                if form.is_valid():
                        instance=form.save(commit=False)
                        instance.author=request.user
                        instance.save()
                        return redirect('/showtodo/')

        else:
                form = forms.todo()
                return render(request, 'createtodo.html', {'form': form})
