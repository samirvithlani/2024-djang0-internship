from django.contrib import admin
#from .models import Blog,Books
from .models import *

# Register your models here.
admin.site.register(Blog)
admin.site.register(Books)
admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Leaves)
admin.site.register(Resources)
admin.site.register(Permissions)
