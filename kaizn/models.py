from django.db import models

# Create your models here.

class Users(models.Model):
    kai_email = models.EmailField(max_length = 100,primary_key=True)
    kai_password = models.CharField(max_length=50)
    # kai_insert_time = models.DateTimeField()
    # kai_isactive = models.BooleanField()


class Items(models.Model):
    kai_SKU = models.CharField(max_length=20,primary_key=True)
    kai_Name = models.CharField(max_length=50)
    kai_Category = models.CharField(max_length=20)
    kai_instock = models.IntegerField()
    kai_available_stock = models.IntegerField()

class Tags(models.Model):
    kai_SKU = models.ForeignKey(Items,related_name="tags",on_delete=models.CASCADE)
    kai_tags = models.CharField(max_length=20)
    class Meta:
        unique_together = (('kai_SKU','kai_tags'),)
