from django.shortcuts import render
from django.views import View
from .database_actions import requests
from django.shortcuts import render


def start(request):
    return render(request, "storage/start.html")


class Inventory(View):
    
    template_name = "storage/inventory.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass



class Storage(View):
    
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass


class Incomming(View):
    
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass


class Outcomming(View):
    
    def get(self, request, *args, **kwargs):
        pass

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