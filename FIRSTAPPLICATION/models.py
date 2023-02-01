from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    phn = models.CharField(max_length=200)
    addr = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    prod_name = models.CharField(max_length=200)
    price = models.IntegerField()
    def __str__(self) -> str:
        return self.prod_name

class orderhist(models.Model):
    order_no = models.IntegerField(primary_key=True)
    cust = models.ForeignKey(Customer, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField()
    def __str__(self) -> str:
        on = str(self.order_no)
        return on