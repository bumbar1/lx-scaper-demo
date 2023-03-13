from django.contrib import admin

from web.models import Listing


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    pass
