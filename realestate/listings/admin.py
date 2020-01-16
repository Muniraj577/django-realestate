from django.contrib import admin
from .models import Category, Property, Events, About, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'subject', 'message')
    list_display_links = ('id', 'name')
    list_per_page = 5


# Register your models here.
admin.site.site_header = 'Real Estate Company'
admin.site.site_title = 'Real Estate Company'
admin.site.register(Category)
admin.site.register(Property)
admin.site.register(Events)
admin.site.register(About)
admin.site.register(Contact, ContactAdmin)
