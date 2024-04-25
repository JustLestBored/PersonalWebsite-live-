from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import redirect

# Create your views here.
def savedata(request):
    if request.method == 'POST':
        user = User.objects.get(id=1)
        form = UserForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('base:admin')
        else:
            print(form.errors)
            return redirect('base:admin')

