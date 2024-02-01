from django.db import models

# Create your models here.


blogGenere = (
    ('Action','Action'),
    ('Comedy','Comedy'),
    ('Drama','Drama'),
    ('Horror','Horror'),
)
class Blog(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    isActive = models.BooleanField(default=True)
    ratings = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    genere = models.CharField(max_length=100,choices=blogGenere)
    country = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.title
    #inner class
    class Meta:
        db_table = "blogs"
        
class Books(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField()
    type = models.CharField(max_length=100)
    
    class Meta:
        db_table = "books"
    
    def __str__(self):
        return self.name    
            