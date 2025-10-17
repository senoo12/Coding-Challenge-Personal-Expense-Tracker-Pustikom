from django.db import models

# Create your models here.
class Category(models.TextChoices):
    food = 'food', 'FOOD'
    transport = 'transport', 'TRANSPORT'
    shoping = 'shoping', 'SHOPING'
    other = 'other', 'OTHER'

class Expenses(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=40, choices=Category.choices)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True) 
    