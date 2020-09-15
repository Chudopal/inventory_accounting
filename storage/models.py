from django.db import models

# Create your models here.

class Storage(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=13)


class IncomingInvoices(models.Model):
    storage = models.ForeignKey(
        'Storage',
        on_delete=models.CASCADE
    )
    date = models.DateField()
    name = models.CharField(max_length=60)
    position = models.CharField(max_length=30)

class IncomingInventorySet(models.Model):
    incoming_invoices = models.ForeignKey(
        'IncomingInvoices',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()


class OutcomingInvoices(models.Model):
    storage = models.ForeignKey(
        'Storage',
        on_delete=models.CASCADE
    )
    date = models.DateField()
    name = models.CharField(max_length=60)
    position = models.CharField(max_length=30)


class OutcomingInventorySet(models.Model):
    incoming_invoices = models.ForeignKey(
        'IncomingInvoices',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()


class FoldingAccounting(models.Model):
    product = models.CharField(max_length=30)
    incoming = models.IntegerField(default=0)
    outcoming = models.IntegerField(default=0)