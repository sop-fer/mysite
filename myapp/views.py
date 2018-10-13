from django.shortcuts import render
from myapp.models import student
# Create your views here.

def index(request):
    studentlist = student.objects.all()
    return render(request, 'myapp/index.html', {'title':'index', 'slist':studentlist})

def market(request,num):
    print(num)
    stu = student.objects.get(pk=num)
    return render(request, 'myapp/market.html', {'title':'market','stu':stu})

def cart(request):
    studentlist = student.objects.all()
    return render(request, 'myapp/cart.html', {'title':'cart', 'slist':studentlist})

def my(request):
    num = request.GET.get('id')
    stu = student.objects.get(pk=num)
    return render(request, 'myapp/my.html', {'title':'my','stu':stu})
