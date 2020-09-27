from django.shortcuts import render
from django.views import View
from .database_actions import requests
from django.shortcuts import render
import json
from django.http import HttpResponse


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
        return HttpResponse("ok")

    def put(self, request, *args, **kwargs):
        inventory = json.loads(request.body)
        requests.update_product(
            column=inventory["column"],
            value=inventory["new_val"],
            id=int(inventory["number"])
        )
        return HttpResponse("ok")

    def delete(self, request, *args, **kwargs):
        inventory = request.headers
        requests.delete_product(
            id=int(inventory["Number"])
        )
        return HttpResponse("ok")


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
        requests.add_storage(
            storage["name"], 
            storage["phone_number"]
        )
        return HttpResponse("ok"), 200

    def put(self, request, *args, **kwargs):
        storage = json.loads(request.body)
        requests.update_product(
            column=storage["column"],
            value=storage["new_val"],
            id=int(storage["number"])
        )
        return HttpResponse("ok")

    def delete(self, request, *args, **kwargs):
        storage = json.loads(request.body)
        requests.delete_storage(
            id=storage["Number"]
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
        incoming = json.loads(request.body)
        requests.add_incoming_invoices(
            incoming["storage_id"],
            incoming["date"],
            incoming["name"],
            incoming["position"]
        )

    def put(self, request, *args, **kwargs):
        incoming = json.loads(request.body)
        requests.update_incoming_invoices(
            column=incoming["column"],
            value=incoming["value"],
            id=int(incoming["id"])
        )

    def delete(self, request, *args, **kwargs):
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
    context = {
        "inventory_set":requests.select_inventory_from_storage(),
    }
    return render(
        request, 
        'storage/list_of_inventory_from_storage.html', 
        context=context
    )


def list_of_incomming_outcomming(request):
    context = {
        "set": requests.select_incomming_and_outcomming()
    }
    return render(
        request,
        "storage/list_of_inventory_from_storage.html",
        context=context
    )
