from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.template import loader
from .models import test
from django.views.generic.edit import CreateView
from .models import Questions
from django.views.generic import ListView
import numpy as np
import pandas as pd
import itertools
import joblib as jb


def testlist(request):
   tests=test.objects.all().values()
   context={
       'tests':tests,
   }
   return render(request,"test.html",context)

def home(request):
    return render(request,'home.html')

def load_test(request):
    indices = Questions.objects.values_list('index')
    qns = Questions.objects.all().values()
    context = {
        'qens':qns , 
        'iindices':indices    
    }
    return render(request,'personality_test.html',context)

def load_master(request):
    return render(request,'predictormaster.html')

def form_handler(request):
    if request.method=='POST':
        data = list(request.POST.values())
        data_mod = list(request.POST.values())
        in_data = np.empty(60)
        data_mod.pop(0)
        data_mod.pop(60)
        x = len(data_mod)
        form_data = np.asarray(data_mod,dtype=int)

        model = jb.load('testapp/best_model.sav')
        
        prediction =  model.predict([form_data])[0]

        context = {
            'prediction':prediction
        }
        return render(request,'test1.html',context)
    else:
        indices = Questions.objects.values_list('index')
        qns = Questions.objects.all().values()
        context = {
        'qens':qns , 
        'iindices':indices    
        }
        return render(request,'personality_test.html',context)
