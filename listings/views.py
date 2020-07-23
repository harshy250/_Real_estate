from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import  bedroom_choices, price_choices, state_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)  #insteal of all we order by date, '-' sign indicates we want reverse order
    #filter is used to filter listings by certain property and in this case it is is_published
    paginator = Paginator(listings, 6)

    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)  #Using is so that if listing id doesn't exit, it shows 404

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)  # 'iexact works for both uppercase and lowercase, exact matches  exact data'

    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)  # 'iexact works for both uppercase and lowercase, exact matches  exact data'

    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)  # lte stands for less than or equal to
    
    # MAX_PRICE
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price) 

    context = {
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)

