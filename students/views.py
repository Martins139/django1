from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,authenticate
from .forms import RegistrationForm
from .models import Records,Myuser
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.hashers import make_password

# Create your views here.
def homepage(request):
    return render(request,'home.html')
def signup(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
       
        if form.is_valid():
            form.save()
            return redirect("/success/")
            
            
            # username = form.cleaned_data.get('username')
            # # raw_password = form.cleaned_data.get('password')
            # # raw_password2=form.cleaned_data.get('password2')
            # first_name=form.cleaned_data.get('first_name')
            # last_name=form.cleaned_data.get('last_name')
            # new_user=Myuser.objects.create(username=username,first_name=first_name,last_name=last_name)
            # new_user.save()
    
       
    return render(request, 'registration.html', {'form':form})
def success(request):
    return render(request,'success.html')
def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/result/')
        else:    
            messages.info(request,'Incorrect Username or password or both')    
    return render(request,'login.html')  
@login_required
def result(request):
    records=Records.objects.filter(user=request.user)
    context={
        "records":records
    }      
    return render(request,'result.html',context)
    

  