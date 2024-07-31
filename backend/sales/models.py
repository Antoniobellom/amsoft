from django.db import models
from phones.models import Phone
from clients.models import Client

class Sale(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sale_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Sale {self.id}"
