from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from users_app.forms import CustomRegisterForm

def register(request):
    if request.method=="POST":
        register_form=CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("New User Account Created, Login to get Started"))
            return redirect('register')
    else:
        register_form=CustomRegisterForm()
    return render(request,'register.html',{'register_form':register_form})
