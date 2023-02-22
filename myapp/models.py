from django.db import models

# Create your models here.


class Student(models.Model):
    product_id = models.AutoField(primary_key=True)
    age = models.CharField(default="", max_length=200)
    personality = models.CharField(max_length=200)
    book = models.CharField(max_length=200, default="")



    # def __str__(self):
    #     return self.


