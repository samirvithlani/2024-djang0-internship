from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    marks = models.FloatField()
    
    class Meta:
        db_table = "student"
    
    def __str__(self):
        return self.name
