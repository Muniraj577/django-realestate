from django.db import models
from django.utils import timezone
from datetime import datetime
# from django.utils.timezone import now
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext as _


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Property(models.Model):
    PROPERTY_TYPE = (
        ('For Sale', _('For Sale')),
        ('For Rent', _('For Rent')),
    )
    title = models.CharField(max_length=250)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    # type = models.BooleanField(default=False)
    # property_type = models.BooleanField(default=0)
    property_type = models.CharField(max_length=10, choices=PROPERTY_TYPE, verbose_name=_('property_type'))
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(timezone.now())
    updated = models.DateTimeField(auto_now=True)
    photo_main = models.ImageField(upload_to='pics')
    photo1 = models.ImageField(upload_to='pics', blank=True)
    photo2 = models.ImageField(upload_to='pics', blank=True)
    photo3 = models.ImageField(upload_to='pics', blank=True)
    photo4 = models.ImageField(upload_to='pics', blank=True)
    photo5 = models.ImageField(upload_to='pics', blank=True)
    photo6 = models.ImageField(upload_to='pics', blank=True)
    photo7 = models.ImageField(upload_to='pics', blank=True)
    photo8 = models.ImageField(upload_to='pics', blank=True)
    photo9 = models.ImageField(upload_to='pics', blank=True)

    class Meta:
        verbose_name = 'property'
        verbose_name_plural = 'properties'

    def __str__(self):
        return self.title


class Events(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    photo = models.FileField(upload_to='pics/events')
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'events'

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    description = RichTextUploadingField(blank=True)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name
