from django.shortcuts import render
from django.http import HttpResponse
from product.models import *

# Create your views here.

def Home(request):
    qs = Product.objects.all()
    context= {
            "qs":qs
        }
    return render(request,'product/home.html',context)
