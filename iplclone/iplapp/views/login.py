from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages

def logout_fun(request):
    logout(request)
    if request.GET:
        return redirect(request.GET['next'])
    return redirect('home')


class Login(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")
        return render(request, template_name="iplapp/login.html")

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.GET:
                return redirect(request.GET['next'])
            return redirect('home')
        messages.error(request,"Invalid Credentials")
        return redirect('login')


class Register(View):

    def get(self, request):
        return render(request,
                      template_name="iplapp/register.html")


    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        try:
            user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
        except Exception as e:
            if e.args[0] == 1062:
                messages.error(request,"Already have an Account")
            else:
                messages.error(request,e)
            return redirect("register")
        if user is not None:
            user.save()
            login(request, user)
            return redirect("home")
        messages.error(request,"cant create user")
