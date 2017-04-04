from django.contrib.auth.models import User
from django.db import models
import os


COVER = {
    (1, 'Twarda'),
    (2, 'Miękka'),
    (3, 'Pudełko'),
    (3, 'Ebook')
}

TYPE = {
    (1, "Podręcznik źródłowy"),
    (2, "Dodatek"),
    (3, "Inne")
}

def get_sys_logo_path(instance, filename):
    return os.path.join('sys_logo', str(instance.id), filename)

def get_publisher_logo_path(instance, filename):
    return os.path.join('publisher_logo', str(instance.id), filename)

def get_book_cover_path(instance, filename):
    return os.path.join('covers', str(instance.id), filename)


# Create your models here.

class System(models.Model):
    sys_logo = models.ImageField(upload_to=get_sys_logo_path, blank=True, null=True)
    name = models.CharField(max_length=256)
    edition = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/system_details/{}".format(self.pk)


class Publisher(models.Model):
    publisher_logo = models.ImageField(upload_to=get_publisher_logo_path, blank=True, null=True)
    name = models.CharField(max_length=32)
    description = models.TextField()
    web_page = models.URLField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/publisher_details/{}".format(self.pk)

class Author(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/author_details/{}".format(self.pk)

class Book(models.Model):
    cover = models.ImageField(upload_to=get_book_cover_path, blank=True, null=True)
    title = models.CharField(max_length=256)
    system = models.ForeignKey(System)
    type = models.IntegerField(choices=TYPE)
    authors = models.ManyToManyField(Author)
    translation = models.CharField(max_length=3000)
    ilustrations = models.CharField(max_length=3000)
    publisher = models.ForeignKey(Publisher)
    pages = models.IntegerField()
    year = models.IntegerField()
    cover_type = models.IntegerField(choices=COVER)
    isbn = models.CharField(max_length=13)
    description = models.TextField()

    def __str__(self):
        return self.title


class Shelf(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)