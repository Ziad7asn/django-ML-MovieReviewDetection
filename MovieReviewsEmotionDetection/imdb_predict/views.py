from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .pipeline.prep_model import pipeline


def predict (request):

    pipe =pipeline()
    pred=''
   
    if request.GET.get('text'):
        text=request.GET.get('text')

        text = pipe.preprocess(text)
        text = pipe.predict(text)
        pred = pipe.post_process(text)
       
        

    return render(request,'home.html',{'txt':f"{pred}"})

