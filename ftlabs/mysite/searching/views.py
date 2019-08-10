from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Engwords
from django.template import loader

def index(request):
    template = loader.get_template('searching/index.html')
    context={'body':'testing',}
    return HttpResponse(template.render(context,request))

def ans1(request):
    return HttpResponse("Type Something...")

def ans(request,s):
    if(len(s)==0):
        return HttpResponse(" ")
    else:
        results_list=Engwords.objects.filter(word__contains=s)
        list_startwith={}
        list_notstartwith={}
        for w in results_list:
            if(w.word.startswith(s)):
                list_startwith[w.word]=w.count
            else:
                list_notstartwith[w.word]=w.count
        result=sorted(list_startwith.items(), key = lambda x : len(x[0]))
        l1=sorted(list_notstartwith.items(), key = lambda x : len(x[0]))
        result.extend(l1)
        result=result[0:25]
        return HttpResponse(result)
        
