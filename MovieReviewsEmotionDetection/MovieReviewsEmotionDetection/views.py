from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from MovieReviewsEmotionDetection.model.prep_model import transform_data ,lr_model,tf


def predict (request):

  
    pred=''
   
    if request.GET.get('text'):
        text=request.GET.get('text')
        text = transform_data(text)
        text = tf.transform([text])
        pred = lr_model.predict(text)

        if pred ==[0]:
            pred = 'Negative'
        else:
            pred = "positive"
        

    return render(request,'home.html',{'txt':f"{pred}"})

