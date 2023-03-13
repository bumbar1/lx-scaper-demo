from django import views

from web.models import Listing


class ListView(views.generic.ListView):
    model = Listing
    template_name = 'listings_list.html'
    queryset = Listing.objects.all()
    context_object_name = 'listings'
    paginate_by = 10


