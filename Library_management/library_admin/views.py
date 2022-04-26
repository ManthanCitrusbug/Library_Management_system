from re import template
from django.shortcuts import render, redirect
from django.views import View
from library_admin.forms import AdminRegisterForm, AdminLoginForm
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class IntexView(TemplateView):
    template_name = 'index.html'


class AdminRegisterView(CreateView):
    model = User
    form_class = AdminRegisterForm
    template_name = 'admin_register.html'
    success_url = ''


class AdminLoginView(View):
    def post(self,request):
        form = AdminLoginForm(request.POST)
        user_name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=user_name,password=password)
        print(user)
        if user is not None: 
            login(request, user)
            return redirect('library_admin:admin-register')
        else:
            return render(request,'admin_login.html',{'form':form}) 

    def get(self,request):
        form = AdminLoginForm()
        return render(request,'admin_login.html',{'form':form})

