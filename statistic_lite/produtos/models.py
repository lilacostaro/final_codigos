from django.db import models

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
