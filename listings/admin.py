from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    #now we cannot click on the title to enter the listing, we have to click the respective 'id' as it is first
    
    list_display_links = ('id', 'title') # To allow us in on clicking the title or any other property

    list_filter=('realtor',)   # To add a filter wrt realtor

    list_editable = ('is_published',)  # To use the is_published button to check and uncheck
    
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price',) # To search wrt fields

    list_per_page = 25


admin.site.register(Listing, ListingAdmin)

