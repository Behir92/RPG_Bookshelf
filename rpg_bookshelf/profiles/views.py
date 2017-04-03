from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views import View
from profiles.forms import AuthForm,RegisterProfileForm
from profiles.models import Profile
# Create your views here.

class IndexView(View):
    def get(self,request):
        return render(request,'library/start.html', {})

class RegisterProfileView(View):

    def get(self,request):
        form = RegisterProfileForm()
        ctx = {'form': form}
        return render(request, 'profiles/register_profile_form.html', ctx)

    def post(self,request):
        form = RegisterProfileForm(data=request.POST)
        ctx = {'form': form}
        if form.is_valid():
            profile = form.save()
            login(request,profile)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'profiles/register_profile_form.html', ctx)

class LoginView(View):
    def get(self,request):
        ctx = {'form': AuthForm()}
        return render(request, 'profiles/login.html', ctx)

    def post(self,request):
        form = AuthForm(data=request.POST)
        ctx = {'form': form}
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'profiles/login.html', ctx)


class LogoutView(View):
    def get (self,request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class ProfileView(View):
    def get(self, request,id):
        profile = User.objects.get(pk=id)
        ctx = {'profile': profile}
        return render(request, 'profiles/profile.html', ctx)