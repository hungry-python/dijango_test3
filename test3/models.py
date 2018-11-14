from django.db import models


class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    phone = models.CharField(max_length=11)
    date = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(null=False)

class Goods(models.Model):
    goodid = models.AutoField(primary_key=True)
    img=models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    userid = models.IntegerField()
