from django.urls import path
from . import views


urlpatterns = [
    path(
        "",
        views.start,
        name="start"
    ),
    path(
        "inventory_actions", 
        views.Inventory.as_view(), 
        name="inventory"
    ),
    path(
        "storage_actions", 
        views.Storage.as_view(), 
        name="storage"
    ),
    path(
        "incommng_actions", 
        views.Incomming.as_view(), 
        name="incomming"
    ),
    path(
        "outcomming_actions",
        views.Outcomming.as_view(),
        name="outcomming"
    ),
    path(
        "in_storage",
        views.list_of_inventory_from_storage,
        name="in_storage"
    ),
    path(
        "incomming_outcomming",
        views.list_of_incomming_outcomming,
        name="incomming_outcomming"
    ),
    path(
        "list_of_storages",
        views.list_of_storages,
        name="storages"
    ),
]
