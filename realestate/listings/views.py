from django.shortcuts import render, get_object_or_404
from .models import Category, Property, About, Contact, Events
from django.core.paginator import Paginator
from django.contrib import messages


# Create your views here.
def index(request, category_slug=None):
    category = None
    categories = Category.objects.filter(name='Top Listings', slug='top-listings')
    properties = Property.objects.filter(available=True, category__name='Top Listings')
    featured = Category.objects.filter(name='Featured Properties', slug='featured-properties')
    featured_properties = Property.objects.filter(available=True, category__name='Featured Properties')
    abouts = About.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        properties = properties.filter(category=categories)
        featured = get_object_or_404(Category, slug=category_slug)
        featured_properties = featured_properties.filter(category=featured)
    context = {'properties': properties,
               'categories': categories,
               'featured_properties': featured_properties,
               'featured': featured,
               'category': category,
               'abouts': abouts
               }
    return render(request, 'listing/index.html', context)


def about(request):
    return render(request, 'listing/about.html')


def detail(request, property_id):
    properties = get_object_or_404(Property, pk=property_id)
    context = {
        'properties': properties,
    }
    return render(request, 'listing/detail.html', context)


def for_sale(request):
    property_list = Property.objects.filter(property_type='For Sale')
    paginator = Paginator(property_list, 6)
    page = request.GET.get('page')
    properties = paginator.get_page(page)
    context = {
        'properties': properties,
    }
    return render(request, 'listing/for-sale.html', context)


def for_rent(request):
    property_list = Property.objects.filter(property_type='For Rent')
    paginator = Paginator(property_list, 6)
    page = request.GET.get('page')
    properties = paginator.get_page(page)
    context = {
        'properties': properties,
    }
    return render(request, 'listing/for-rent.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name, email=email, phone=phone, subject=subject, message=message)
        contact.save()
        messages.success(request, 'Your message has been submitted.')
    return render(request, 'listing/contact.html')


def events(request):
    event_list = Events.objects.all()
    paginator = Paginator(event_list, 4)
    page = request.GET.get('page')
    events = paginator.get_page(page)
    context = {
        'events': events,
    }
    return render(request, 'listing/events.html', context)


def event_detail(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    context = {
        'event': event,
    }
    return render(request, 'listing/event-detail.html', context)


def search(request):
    queryset_list = Property.objects.all()
    paginator = Paginator(queryset_list, 4)
    page = request.GET.get('page')
    listings = paginator.get_page(page)

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(title__icontains=keywords)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__exact=price)

    if 'property_type' in request.GET:
        property_type = request.GET['property_type']
        if property_type:
            queryset_list = queryset_list.filter(property_type__exact=property_type)

    context = {
        'properties': queryset_list,
        'values': request.GET,
        'listings': listings,
    }

    return render(request, 'listing/search.html', context)
