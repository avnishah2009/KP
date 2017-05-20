from django.conf.urls import url
from views import (Home,
                   ItemList,
                   StoreList,
                   StoreListReact,
                   StoreDetail,
                   TripDetail,
                   ShoppingTripDetail)
    # GroceryList,  , AddStore, AddItem

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    # url(r'^list/$', GroceryList.as_view(), name='grocery_list'),
    url(r'^items/$', ItemList.as_view(), name='item_list'),
    url(r'^stores/$', StoreList.as_view(), name='store_list'),
    url(r'^react_stores$', StoreListReact.as_view(), name='store_list_react'),
    url(r'^shopping_trips/$', TripDetail.as_view(), name='trip_list'),
    url(r'^store_details/(?P<store_name>[a-zA-Z0-9-]+)$', StoreDetail.as_view(), name='store_detail'),
    url(r'^shopping_trip_detail/$', ShoppingTripDetail.as_view(), name='shopping_trip_detail'),
    ]
