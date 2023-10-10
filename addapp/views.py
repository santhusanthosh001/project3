from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"saa.html")
def santhu (request):
    i = request.GET["t1"]
    j = request.GET["t2"]
    x = int(i)
    y = int(j)
    z = x+y
    res = HttpResponse("the sum value is: "+str(z))
    return res

