from django.urls import path
from . import views

app_name="storage"

urlpatterns = [
    path(
        "",
        views.start,
        name="start"
    ),
    path(
        "inventory_actions", 
        views.inventory, 
        name="inventory"
    ),
    path(
        "storage_actions", 
        views.storage, 
        name="storage"
    ),
    path(
        "incommng_actions", 
        views.incomming, 
        name="incomming"
    ),
    path(
        "outcomming_actions",
        views.outcomming,
        name="outcomming"
    )
    path(
        "in_storage",
        views.list_of_inventory_from_storage
        name="in_storage"
    )
    path(
        "incomming_outcomming",
        views.list_of_incomming_outcomming,
        name="incomming_outcomming"
    )
    path(
        "list_of_storages",
        views.list_of_storages,
        name="storages"
    )
]
