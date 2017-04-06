from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView
from profiles.forms import AuthForm,RegisterProfileForm
from profiles.models import Profile
# Create your views here.


class RegisterProfileView(View):

    def get(self,request):
        form = RegisterProfileForm()
        ctx = {'form': form}
        return render(request, 'profiles/register_profile_form.html', ctx)

    def post(self,request):
        form = RegisterProfileForm(data=request.POST)
        ctx = {'form': form}
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            login(request,user)
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
    def get(self, request,profile_id):
        profile = Profile.objects.get(pk=profile_id)
        user = User.objects.get(pk=profile.user.id)
        ctx = {'profile': profile,
               'user': user}
        return render(request, 'profiles/profile.html', ctx)

class UpdateProfileView(UpdateView):
    template = 'profiles/profile_form.html'
    model = Profile
    fields = ['nick','avatar','fav_system']

class UpdateUserView(UpdateView):
    template = 'profile/user_form.html'
    model = User
    fields = ['email','first_name','last_name']