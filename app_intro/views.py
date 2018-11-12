from django.shortcuts import render
import random
# Create your views here.

def index(request):
    return render(request,'index.html')
    
def lunch(request):
    menu_list=['20','kimbab','sigol']
    pick=random.choice(menu_list)
    return render(request,'lunch.html',{'pick':pick})

def lotto(request):
    pick=random.sample(range(1,46),6)
    return render(request,'lotto.html',{'pick':pick})

def hello(request,name):
    return render(request,'hello.html',{'name':name})
    
def cube(request,num):
    multi=num**3
    return render(request,'cube.html',{'multi':multi})
    