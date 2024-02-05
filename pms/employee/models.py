from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    password = models.CharField(max_length=100)
    salary = models.FloatField()
    
    class Meta:
        db_table = "employees"
    
    def __str__(self):
        return self.name    