from django.shortcuts import render

# Create your views here.

def for_loop(request):
    d={'name':'Sai Dasaradha','age':21}
    return render(request,'forloop.html',d)