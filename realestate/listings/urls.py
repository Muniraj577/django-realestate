from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('property/<int:property_id>', views.detail, name='detail'),
    path('for-sale', views.for_sale, name='for-sale'),
    path('for-rent', views.for_rent, name='for-rent'),
    path('contact', views.contact, name='contact'),
    path('events', views.events, name='events'),
    path('event-detail', views.event_detail, name='event-detail'),
    path('event/<int:event_id>', views.event_detail, name='event-detail'),
    path('search', views.search, name='search'),
]
