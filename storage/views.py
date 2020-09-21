from django.shortcuts import render
from django.views import View
from .database_actions import requests
from django.shortcuts import render
import json


def start(request):
    return render(request, "storage/start.html")


class Inventory(View):

    template_name = "storage/inventory.html"

    def get(self, request, *args, **kwargs):
        inventory_set = requests.select_product()
        context = {
            "inventory_set": inventory_set
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        inventory = json.loads(request.body)
        requests.add_product(inventory["name"])

    def put(self, request, *args, **kwargs):
        inventory = json.loads(request.body)
        requests.update_product(
            column=int(inventory["column"]),
            value=inventory["value"],
            id=int(inventory["id"])
        )

    def delete(self, request, *args, **kwargs):
        inventory = json.loads(request.body)
        requests.delete_product(
            id=inventory["id"]
        )


class Storage(View):

    template_name = "storage/storage.html"
    
    def get(self, request, *args, **kwargs):
        storage_set = requests.select_storage(order_by="name")
        context = {
            "storage_set": storage_set
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        storage = json.loads(request.body)
        requests.add_storage(storage["name"], storage["phone_number"])

    def put(self, request, *args, **kwargs):
        storage = json.loads(request.body)
        requests.update_product(
            column=int(storage["column"]),
            value=storage["value"],
            id=int(storage["id"])
        )

    def delete(self, request, *args, **kwargs):
        storage = json.loads(request.body)
        requests.delete_storage(
            id=storage["id"]
        )


class Incoming(View):
    
    template_name = "storage/incoming.html"

    def get(self, request, *args, **kwargs):
        incoming = requests.select_incoming_invoices()
        context = {
            "incoming_set": incoming
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass


class Outcoming(View):
    
    template_name = "storage/incoming.html"

    def get(self, request, *args, **kwargs):
        outcoming = requests.select_outcoming_invoices()
        context = {
            "outcoming_set": outcoming
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass


def list_of_inventory_from_storage(request):
    pass


def list_of_incomming_outcomming(request):
    pass


def list_of_storages(request):
    pass