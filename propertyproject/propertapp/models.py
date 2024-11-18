from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass
    def __str__(self):
         return self.username

class Address(models.Model):
     strict=models.CharField(max_length=30)
     city=models.CharField(max_length=30)
     class Meta:
         verbose_name='Address'
         verbose_name_plural='Addresses'

class Property(models.Model):
    address=models.ForeignKey(Address,on_delete=models.RESTRICT)
    name=models.CharField(max_length=200)
    type=models.CharField(max_length=50)
    value=models.IntegerField()
    class Meta:
        verbose_name='Property'
        verbose_name_plural='Properties'


class Ternant(models.Model):
        names=models.CharField(max_length=100)
        phone=models.IntegerField()
        email=models.CharField(max_length=50)
        class Meta:
          verbose_name='ternant'
          verbose_name_plural='Ternants'


class Lease(models.Model):
     names=models.CharField(max_length=150)
     phone=models.IntegerField()
     email=models.CharField(max_length=70)
     class Meta:
         verbose_name='Lease'
         verbose_name_plural='Leases'

class Contract(models.Model):
     start_date=models.DateField()
     end_date=models.DateField()
     content=models.FileField(upload_to ='contract',null=True)
     class Meta:
         verbose_name='Contract'
         verbose_name_plural='Contracts'




