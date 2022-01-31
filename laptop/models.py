from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=30)


class Laptop(models.Model):
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    GPU = models.CharField(max_length=50)
    graphics_card = models.CharField(max_length=50)
    RAM = models.CharField(max_length=50)
    memory = models.CharField(max_length=50)
    display = models.CharField(max_length=255)
    date = models.DateTimeField()
    price = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Gadget(models.Model):  # for laptop
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

