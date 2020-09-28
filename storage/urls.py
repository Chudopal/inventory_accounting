from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
        "incoming_actions", 
        views.Incoming.as_view(), 
        name="incoming"
    ),
    path(
        "incoming_actions/<int:pk>", 
        views.IncomingSet.as_view(), 
        name="incoming_set"
    ),
    path(
        "outcoming_actions",
        views.Outcoming.as_view(),
        name="outcoming"
    ),
    path(
        "in_storage",
        views.list_of_inventory_from_storage,
        name="in_storage"
    ),
    path(
        "incoming_outcoming",
        views.list_of_incomming_outcomming,
        name="incoming_outcoming"
    ),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)