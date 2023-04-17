from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate , logout
from django.contrib import messages
from client.models import AddpostModel
from client.models import add_question
from django.contrib.auth import get_user_model

# Create your views here.


def index(request):
    Allposts=AddpostModel.objects.all()
    Allquestions=add_question.objects.all()
    return render(request, 'index.html' , {'Allposts' : Allposts , 'Allquestions' : Allquestions})


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'signup.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    print("into login in function")
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user :
                login(request, user)
                return redirect('index')
            else:
                msg= 'Worng credential / Please check your credential'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})



def freelancer(request):
    return render(request,'freelancer.html')


def client(request):
    return render(request,'client.html')
    
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")
	
def account(request):
    return render(request, 'account.html')