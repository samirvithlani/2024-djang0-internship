from django.db import models

# Create your models here.
procat = (
    ('Electronics','Electronics'),
    ('Clothes','Clothes'),
    ('Grocery','Grocery')
)
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    qty = models.IntegerField()
    discount = models.FloatField()
    status = models.BooleanField(default=True)
    cat = models.CharField(max_length=100,choices=procat)
    
    class Meta:
        db_table = "product"
    
    def __str__(self):
        return self.name    
    