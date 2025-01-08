import threading
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.shortcuts import render
from django.http import HttpResponse

from . import models
from . import forms


def save_video_to_cloud(file, instance):
    file_path = default_storage.save(file.name, ContentFile(file.read()))
    instance.file = file_path
    instance.save()



def home_view(request):

    videos = models.VideoModel.objects.all()

    context = {
        'videos':videos,
    }
    return render(request,'home.html',context=context)

def form_view(request):
    form = forms.VideoForm()
    context = {
        'form':form,
    }
    if request.method == "GET":
        return render(request,'form.html',context=context)

    elif request.method == "POST":
        instance = forms.VideoForm(data=request.POST,files=request.FILES)
        file = request.FILES['video']

        
        thread = threading.Thread(target=save_video_to_cloud,args=(file,instance,))
        thread.start()

        return HttpResponse("Your video save")