from django.shortcuts import render
from django.http import HttpResponse

from .models import Customer

# Create your views here.
def detail(request):

    q = Customer.objects.all()
    context = {
        'data': q
    }
    return render(request,'customer/index.html',context)
