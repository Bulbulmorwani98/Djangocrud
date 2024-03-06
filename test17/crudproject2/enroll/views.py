from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.
# This function will add the new user and show the users.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print(fm)
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            print(nm)
            reg = User(name=nm,email=em,password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html',{'form':fm,'stu':stud})

# This Function will Update


def update_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')
    else:
        pi=User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)

        return render(request, 'enroll/updatestudent.html',{'form':fm})

# def update_show(request):
#      if request.method == 'POST':
#           email = request.POST.get('email')
#           name = request.POST.get('name')
#           password = request.POST.get('password')

#           user = User.objects.get(email=email)

#           # Update the user's name and password
#           user.name = name
#           user.password = password

#           user.save()
         
#           return HttpResponseRedirect('/')





# This function will Delete.
def delete_data(request, id):
    if request.method == 'POST':
        print('==========')
        pi = User.objects.get(id=id)
        pi.delete()
        return HttpResponseRedirect('/')
    