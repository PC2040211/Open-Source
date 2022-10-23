from django.http import HttpResponse
from django.shortcuts import render 
from django.http import HttpResponse
from .models import Image
# form 

# Create your views here.
def image(request,Image):
    print(Image)
    return HttpResponse("yours image" %Image)