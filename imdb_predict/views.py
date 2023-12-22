from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.template.loader import render_to_string 
from .forms import FileForm
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



def upload_file(request):
    pipe = pipeline()
    if request.method =='POST':
        request.FILES.file='review_123.csv'
        form = FileForm(request.POST,request.FILES)
        
        if form.is_valid():
            
            file_path=form.save()
            pipe.predict_csv_file(file_path.file.path)
            return redirect('home')
    else:
        form = FileForm()
    
    return render(request,'model_form_upload.html',{'form':form})


