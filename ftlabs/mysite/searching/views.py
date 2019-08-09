from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Engwords

def index(request,s):
    results_list=Engwords.objects.filter(word__contains=s)
    list_startwith={}
    list_notstartwith={}
    for w in results_list:
        if(w.word.startswith(s)):
            list_startwith[w.word]=w.count
        else:
            list_notstartwith[w.word]=w.count
    l=sorted(list_startwith.items(), key = lambda x : len(x[0]))
    l1=sorted(list_notstartwith.items(), key = lambda x : len(x[0]))
    l.extend(l1)
    return HttpResponse(l[0:25])
