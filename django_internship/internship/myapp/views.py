from django.db import models
from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic import ListView
from.models import Student 

def homepage(request):
    return render(request,'home.html')

def aboutpage(request):
    return render(request, 'about.html')

def contactpage(request):
    return render(request, 'contact.html')

def form(request):
    return render(request, 'form.html')
def process(request):
    
    a = int(request.POST['txt1'])
    b = int(request.POST['txt2'])
    c = a + b
    #print(c)
    return render(request, 'ans.html',{'mysum':c, 'mya':a, 'myb':b})


class Studentlist(ListView):
    model = Student
    template_name = 'studentlist.html'
 