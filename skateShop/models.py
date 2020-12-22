# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=200)



class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

