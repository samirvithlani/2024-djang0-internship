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
 

class Director(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    exp = models.IntegerField()
    
    class Meta:
        db_table = "directors"
    def __str__(self):
        return self.name


class Movie(Director):
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    isActive = models.BooleanField(default=True)
    ratings = models.FloatField()
    
    class Meta:
        db_table = "movies"
        
    def __str__(self):
        return self.title


class Course(models.Model):
    name = models.CharField(max_length=100)
    fees = models.IntegerField()
    duration = models.IntegerField()
    
    class Meta:
        db_table = "courses"
        
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course  = models.ForeignKey(Course,on_delete=models.CASCADE) #course_id           
    
    class Meta:
        db_table = "students"
    def __str__(self):
        return self.name


#many to many relationship        

class Leaves(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    
    class Meta:
        db_table = "leaves"

    def __str__(self):
        return self.name


class Permissions(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    class Meta:
        db_table = "permissions"
    def __str__(self):
        return self.name        

class Resources(models.Model):
    name= models.CharField(max_length=100)
    leaves = models.ManyToManyField(Leaves)
    permissions = models.ManyToManyField(Permissions,null=True,blank=True)
    
    class Meta:
        db_table = "resources"
    def __str__(self):
        return self.name    
    
            