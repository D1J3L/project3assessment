from django.db import models
from django.forms import IntegerField

# Create your models here.
class Widget(models.Model):
    description = models.CharField(max_length=50)
    quantity = IntegerField()

    def __str__(self):
        return self.item