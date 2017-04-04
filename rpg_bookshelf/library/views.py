from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from .models import (
    Author,
    Publisher,
    System
)
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView, CreateView

# Create your views here.

class SystemListView(View):
    def get(self,request):
        systems = System.objects.all().order_by('name')
        ctx = {'systems': systems}
        return render(request, 'library/system_list.html', ctx)

class SystemView(View):
    def get(self,request,pk):
        system = System.objects.get(pk=pk)
        ctx = {'system': system}
        return render(request, 'library/system_details.html', ctx)

class AddSystemView(LoginRequiredMixin,CreateView):
    model = System
    fields = '__all__'
    success_url = '/systems/'

class ChangeSystemView(PermissionRequiredMixin,UpdateView):
    permission_required = ['library.change_system']
    model = System
    fields = '__all__'

class PublisherListView(View):
    def get(self,request):
        publishers = Publisher.objects.all().order_by('name')
        ctx = {'publishers': publishers}
        return render(request, 'library/publisher_list.html', ctx)

class PublisherView(View):
    def get(self,request,pk):
        publisher = Publisher.objects.get(pk=pk)
        ctx = {'publisher': publisher}
        return render(request, 'library/publisher_details.html', ctx)

class AddPublisherView(LoginRequiredMixin,CreateView):
    model = Publisher
    fields = '__all__'
    success_url = '/publishers/'

class ChangePublisherView(PermissionRequiredMixin,UpdateView):
    permission_required = ['library.change_publisher']
    model = Publisher
    fields = '__all__'

class AuthorListView(View):
    def get(self,request):
        authors = Author.objects.all().order_by('name')
        ctx = {'authors': authors}
        return render(request, 'library/author_list.html', ctx)

class AuthorView(View):
    def get(self,request,pk):
        author = Author.objects.get(pk=pk)
        ctx = {'author': author}
        return render(request, 'library/author_details.html', ctx)

class AddAuthorView(LoginRequiredMixin,CreateView):
    model = Author
    fields = '__all__'
    success_url = '/authors/'

class ChangeAuthorView(PermissionRequiredMixin,UpdateView):
    permission_required = ['library.change_author']
    model = Author
    fields = '__all__'