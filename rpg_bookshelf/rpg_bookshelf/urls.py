"""rpg_bookshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from library.views import (
AddAuthorView,
AddBookToShelfView,
AddBookView,
AddPublisherView,
AddSystemView,
AuthorListView,
AuthorView,
BookListView,
BookView,
ChangeAuthorView,
ChangeBookView,
ChangePublisherView,
ChangeSystemView,
DeleteBookFromShelf,
IndexView,
PublisherView,
PublisherListView,
SystemView,
SearchView,
SystemListView,
ShelfView

)
from profiles.views import (
    LoginView,
    LogoutView,
    ProfileView,
    RegisterProfileView,
    UpdateProfileView,
    UpdateUserView,
)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register$', RegisterProfileView.as_view(), name='register-profile'),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
    url(r'^profile/(?P<profile_id>(\d+))$', ProfileView.as_view(), name='profile'),
    url(r'^update_profile/(?P<pk>(\d+))$', UpdateProfileView.as_view(), name='update-profile'),
    url(r'^update_user/(?P<pk>(\d+))$', UpdateUserView.as_view(), name= 'update-user'),
    url(r'^systems/$', SystemListView.as_view(), name='system-list'),
    url(r'^system_details/(?P<pk>(\d+))$', SystemView.as_view(), name='system-details'),
    url(r'^add_system/$', AddSystemView.as_view(), name='add-system'),
    url(r'^change_system/(?P<pk>(\d+))$', ChangeSystemView.as_view(), name='change-system'),
    url(r'^publishers/$', PublisherListView.as_view(), name='publisher-list'),
    url(r'^publisher_details/(?P<pk>(\d+))$', PublisherView.as_view(), name='publisher-details'),
    url(r'^add_publisher/$', AddPublisherView.as_view(), name='add-publisher'),
    url(r'^change_publisher/(?P<pk>(\d+))$', ChangePublisherView.as_view(), name='change-publisher'),
    url(r'^authors/$', AuthorListView.as_view(), name='author-list'),
    url(r'^author_details/(?P<pk>(\d+))$', AuthorView.as_view(), name='author-details'),
    url(r'^add_author/$', AddAuthorView.as_view(), name='add-author'),
    url(r'^change_author/(?P<pk>(\d+))$', ChangeAuthorView.as_view(), name='change-author'),
    url(r'^books/$', BookListView.as_view(), name='book-list'),
    url(r'^book_details/(?P<pk>(\d+))$', BookView.as_view(), name='book-details'),
    url(r'^add_book/$', AddBookView.as_view(), name='add-book'),
    url(r'^change_book/(?P<pk>(\d+))$', ChangeBookView.as_view(), name='change-book'),
    url(r'search_results/', SearchView.as_view(), name='search'),
    url(r'shelf/(?P<user_id>(\d+))$', ShelfView.as_view(), name='shelf'),
    url(r'shelf/add/(?P<book_id>(\d+))$', AddBookToShelfView.as_view(), name='shelf-add'),
    url(r'shelf/delete/(?P<pk>(\d+))$', DeleteBookFromShelf.as_view(), name='shelf-delete'),
]