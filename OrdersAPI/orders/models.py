from django.db import models

# Create your models here.

class Order_Detail(models.Model):
    user_id = models.CharField(max_length=15)
    product_id = models.CharField(max_length=15)
    quantity = models.IntegerField()
    payment_information = models.CharField(max_length=15)

    def __str__(self):
        return self.product_id