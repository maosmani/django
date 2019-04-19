from django.db import models



class Product(models.Model):
	product_name = models.CharField(max_length=100)
	product_id = models.CharField(max_length=100)