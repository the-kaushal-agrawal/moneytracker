from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(primary_key=True,max_length=100,default="")
    

    def __str__(self):
        return self.name

class TranscationsData(models.Model):
    member = models.ManyToManyField(User,related_name="spliters")
    date = models.DateField()
    amount = models.FloatField(default=0)
    paidby = models.ForeignKey(User,related_name="paidby", on_delete = models.CASCADE,to_field="username")
    category = models.ForeignKey(Category,on_delete=models.CASCADE)





