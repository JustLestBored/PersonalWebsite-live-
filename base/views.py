from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from cms.models import *
from django.core.mail import send_mail

# Create your views here.

def home(request):
    user = User.objects.get(id=1)
    context = {'user':user}
    return render(request,'home.html',context)

def abouts(request):
    user = User.objects.get(id=1)
    context = {'user':user}
    return render(request,'About.html',context)
    
def resume(request):
    user = User.objects.get(id=1)
    context = {'user':user}
    return render(request,'resume.html',context)

def contact(request):
    if request.method == 'POST':
        user_instance = User.objects.first()
        email = user_instance.email
        email_address = request.POST['email_address']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(subject, message, email_address, [email] )
    return render(request,'contact.html')

def gallery(request):
    return render(request,'gallery.html')

def project(request):
    return render(request,'project.html')

def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        user=authenticate(username=username, password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('base:admin')
         
    return render(request,'Admin/login.html')


def logout(request):
    auth_logout(request)
    return redirect ('base:login')


def admin(request):
    if request.user.is_authenticated:
        user = User.objects.get(username='admin')
        context = {'user':user}
        return render(request,'Admin/admin.html',context)
    else:
        return redirect ('base:login')



def contactMe(subject, message, email_address, email, fail_silently=False):
    try:
        send_mail(subject, message, email_address, [email], fail_silently=fail_silently)
    except Exception as e:
        print(f"Error sending email: {e}") 

    return render()
        
        