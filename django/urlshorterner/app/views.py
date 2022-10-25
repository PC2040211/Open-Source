from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import pyshorteners


# Create your views here.
class Url(View):
    def post(self,request):
        long='url' in request.POST and request.POST['url']
        psy=pyshorteners.Shortener()
        short=psy.tinyurl.short(long)
    # return  HttpResponse("HO gya bhai")
        return render(request,'index.html',{'long':long,'short':short})
 
    def get(self,request):
        return render(request,'index.html')
        # return  render(request,"index.html",{'url1':url1})