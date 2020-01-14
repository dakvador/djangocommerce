from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from datetime import datetime


CATEGORY_CHOICES=(
    ('Sh','Shirt'),
    ('P', 'Pants'),
    ('Sw','Sweater'),
    ('So', 'Shoes'),
)


class Item(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, default="P")
    description = models.TextField(null=True, blank=True)
    photo = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default = 1)



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(default = datetime.now())
    total = models.FloatField(default=0)

