from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.views import View
from django.views.generic import ListView
from django.views.generic.base import RedirectView
from models import Trip, Item, Store, TripItem

class Home(View):

    def get(self, *args, **kwargs):
        print "This gets a hit"
        return HttpResponseRedirect("/khaana-peena/shopping_trips")

class ItemList(ListView):
    model = Item
    context_object_name = 'items'


class StoreList(ListView):
    model = Store
    context_object_name = 'stores'
    # The template is automatically located
    # in templates/groceriesapp/class_name.html file

class StoreListReact(ListView):
    template_name = "store_list_react.html"
    def get(self, request):
        stores = Store.objects.all()
        store_list = [store.name for store in stores]
        store_dict = {}
        store_dict["store"] = store_list
        # return render(request, self.template_name, locals())
        return JsonResponse(store_list, safe=False)



class StoreDetail(ListView):
    template_name = "store_detail.html"
    def get(self, request, store_name):
        print store_name
        store = Store.objects.get(name=store_name)
        last_trip = Trip.objects.filter(store=store).order_by("-date")
        print last_trip
        trip_items = TripItem.objects.filter(trip=last_trip)
        print trip_items
        return render(request, self.template_name, locals())

class TripDetail(ListView):
    template_name = "trip_detail.html"

    def get(self, request):
        store = Store.objects.get(name="New India Bazaar - Milpitas")
        trip = Trip.objects.filter(store=store)[0]
        trips = Trip.objects.filter().order_by("-date")
        trip_items = TripItem.objects.filter(trip=trip)
        return render(request, self.template_name, locals())


class ShoppingTripDetail(ListView):
    template_name = "shopping_trip_detail.html"

    def get(self, request):
        store = Store.objects.get(name="New India Bazaar - Milpitas")
        trip = Trip.objects.filter(store=store)[0]
        trips = Trip.objects.filter().order_by("-date")
        trip_items = TripItem.objects.filter(trip=trip)
        return render(request, self.template_name, locals())