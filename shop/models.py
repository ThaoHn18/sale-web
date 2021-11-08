from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=150)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=150)
    description = models.TextField()
    image = models.CharField(max_length=300)

    # class Meta:
    #    ordering = ['-id']
    def __str__(self):
        return self.title


class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=100)
    total= models.FloatField()



    def __str__(self):
        return self.name
    