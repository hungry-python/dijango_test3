from django.shortcuts import render
from test3.models import User,Goods
def index1(request):
    users=User.objects.all()
    return render(request,'index.html',{'users':users})
def index2(request):
    goods=Goods.objects.all()
    return render(request,'index2.html',{'goods':goods})
# Create your views here.
