from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello World")

def aboutUs(request):
    print(request)
    return render(request,"aboutUs.html")


def contactUs(request):
    print(request)
    name = "Royal"
    age = 20
    context = {
        "name":name,
        "age":age
    }
    #return render(request,"blog/contactUs.html",{"name":name})
    return render(request,"blog/contactUs.html",context)