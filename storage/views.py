from django.shortcuts import render
from django.views import View
from .database_actions import requests
from django.shortcuts import render
import json
from django.http import HttpResponse
from datetime import datetime


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
            "incoming": incoming
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        incoming = json.loads(request.body)
        requests.add_incoming_invoices(
            incoming["storage_number"],
            datetime.strftime(datetime.now(), "%Y.%m.%d"),
            incoming["name"],
            incoming["position"]
        )
        return HttpResponse("ok"), 200

    def put(self, request, *args, **kwargs):
        incoming = json.loads(request.body)
        requests.update_incoming_invoices(
            column=incoming["column"],
            value=incoming["value"],
            id=int(incoming["id"])
        )
        return HttpResponse("ok"), 200

    def delete(self, request, *args, **kwargs):
        incom = json.loads(request.body)
        requests.delete_incoming_invoices(
            id=incom["Number"]
        )
        return HttpResponse("ok"), 200


class IncomingSet(View):
    
    def get(self, request, pk):
        incoming_set = requests.select_incoming_inventory_set(
            conditions=[
                f"incoming_invoices_id={pk}"
            ]
        )
        context = {
            "incoming_set": incoming_set
        }
        return render(request, "storage/incoming_set.html", context)

    def post(self, request, pk):
        incoming_set = json.loads(request.body)
        requests.add_incoming_inventory_set(
            int(pk),
            int(incoming_set["product_id"]),
            int(incoming_set["quantity"])
        )
        folding = list(requests.select_folding_accounting(
            conditions=[
                f"product_id={int(incoming_set['product_id'])}",
            ]
        )[0])
        if not folding:
            storage_id = int((requests.select_incoming_invoices(
                    conditions=[
                        f"id={pk}"
                    ]
                )
            )[0][4])
            requests.add_folding_accounting(
                storage_id,
                int(incoming_set["product_id"]),
                int(incoming_set["quantity"]),
                0
            )
        else: 
            requests.update_folding_accounting(
                "incoming",
                folding[1] + int(incoming_set["quantity"]),
                folding[0]
            )

        return HttpResponse("ok"), 200
    
    def put(self, request, pk):
        incoming_set = json.loads(request.body)
        requests.update_incoming_inventory_set(
            column=incoming_set["column"],
            value=incoming_set["value"],
            id=int(incoming_set["id"])
        )
        return HttpResponse("ok"), 200

    def delete(self, request, pk):
        incoming_set = json.loads(request.body)
        requests.delete_incoming_inventory_set(
            id=incoming_set["Number"]
        )
        return HttpResponse("ok"), 200


class Outcoming(View):
    
    template_name = "storage/outcoming.html"

    def get(self, request, *args, **kwargs):
        outcoming = requests.select_outcoming_invoices()
        context = {
            "outcoming": outcoming
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        outcoming = json.loads(request.body)
        requests.add_outcoming_invoices(
            outcoming["storage_number"],
            datetime.strftime(datetime.now(), "%Y.%m.%d"),
            outcoming["name"],
            outcoming["position"]
        )
        return HttpResponse("ok"), 200

    def put(self, request, *args, **kwargs):
        outcoming = json.loads(request.body)
        requests.update_outcoming_invoices(
            column=outcoming["column"],
            value=outcoming["value"],
            id=int(outcoming["id"])
        )
        return HttpResponse("ok"), 200

    def delete(self, request, *args, **kwargs):
        outcom = json.loads(request.body)
        requests.delete_outcoming_invoices(
            id=outcom["Number"]
        )
        return HttpResponse("ok"), 200



class OutcomingSet(View):
    
    def get(self, request, pk):
        outcoming_set = requests.select_outcoming_inventory_set(
            conditions=[
                f"incoming_outvoices_id={pk}"
            ]
        )
        context = {
            "outcoming_set": outcoming_set
        }
        return render(request, "storage/outcoming_set.html", context)

    def post(self, request, pk):
        outcoming_set = json.loads(request.body)
        requests.add_outcoming_inventory_set(
            int(pk),
            int(outcoming_set["product_id"]),
            int(outcoming_set["quantity"])
        )
        folding = list(requests.select_folding_accounting(
            conditions=[
                f"product_id={int(outcoming_set['product_id'])}",
            ]
        )[0])
        if not folding:
            storage_id = int((requests.select_outcoming_invoices(
                    conditions=[
                        f"id={pk}"
                    ]
                )
            )[0][4])
            requests.add_folding_accounting(
                storage_id,
                int(outcoming_set["product_id"]),
                int(outcoming_set["quantity"]),
                0
            )
        else: 
            requests.update_folding_accounting(
                "incoming",
                folding[1] + int(outcoming_set["quantity"]),
                folding[0]
            )

        return HttpResponse("ok"), 200
    
    def put(self, request, pk):
        outcoming_set = json.loads(request.body)
        requests.update_outcoming_inventory_set(
            column=outcoming_set["column"],
            value=outcoming_set["value"],
            id=int(outcoming_set["id"])
        )
        return HttpResponse("ok"), 200

    def delete(self, request, pk):
        outcoming_set = json.loads(request.body)
        requests.delete_outcoming_inventory_set(
            id=outcoming_set["Number"]
        )
        return HttpResponse("ok"), 200


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

