from django.shortcuts import render
from .forms import ProductForm
from django.http import HttpResponseRedirect
from .models import Product

# Create your views here.
def create_product(request):
    context = {} #empty dictionary
    form = ProductForm(request.POST or None)
    context["form"] = form #passing form to context to create form in template
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/product/list/")
    
    return render(request,"products/product_create.html",context)


def list_product(request):
    context = {} #empty dictionary
    products = Product.objects.all().values() #select * from product
    context["products"] = products
    
    return render(request,"products/product_list.html",context)

def detail_product(request,id):
    contect = {}
    product = Product.objects.get(id=id)
    contect["product"] = product
    
    return render(request,"products/product_detail.html",contect)


def delete_product(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return HttpResponseRedirect("/product/list/")

def update_product(request,id):
    context = {}
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None,instance=product)
    context["form"] = form
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/product/list/")
    
    
    return render(request,"products/product_update.html",context)
    
    