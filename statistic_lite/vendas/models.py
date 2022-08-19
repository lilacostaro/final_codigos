from django.db import models

# Create your models here.

PAYMENT_CHOICES = (
    ('Money', 'Dinheiro'),
    ('Credit', 'Credito'),
    ('Debit', 'Debito'),
    ('Pix', 'Pix')
)

class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True)
    full_price = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.CharField(max_length=8, choices=PAYMENT_CHOICES)
    card_info = models.CharField(max_length=16)
    sela_data = models.DateField(auto_now=True)

class Detailed_sale(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)