from django.shortcuts import render,HttpResponseRedirect
from .forms import RegistrationForm
from .models import User
# Create your views here.

def home(request):
    return render(request, 'info/home.html')


def add_info(request):
    print('*********************')
    if request.method == "POST":

        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ag = fm.cleaned_data['age']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, age=ag, password=pw)
            reg.save()
            fm = RegistrationForm()
            return render(request, 'info/home.html')
    else:
        fm = RegistrationForm()
    return render(request, 'info/signup.html',{'form':fm})


def login(request):
   return render(request, 'info/login.html')

def loginrecord(request):
    #  is used to check if the current request is a POST request, meaning the user has submitted a form.
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        # return render(request,'info/dashboard.html')

        pi = User.objects.get(email=email)
        if pi.email == email and pi.password == password:
            return render(request, 'info/dashboard.html',{'form':pi} )
    return render(request, 'info/login.html')


def delete(request, id):
        print('======================')
        pi = User.objects.get(id=id)
        print('jjjjjjjjjjjjjjjjjjjjjjjj')
        pi.delete()
        return HttpResponseRedirect('/')

def update(request, id):
    if request.method == "POST":
        print('===========================',id)
        pi = User.objects.get(id=id)
        fm = RegistrationForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')

        
    else:
        pi = User.objects.get(id=id)
        fm = RegistrationForm(instance=pi)
        print('*******************')
        return render(request, 'info/updateuser.html',{'form':fm})
    
# def updateshow(request)
