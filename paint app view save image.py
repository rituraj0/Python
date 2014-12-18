# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from paintapp.models import Files
from django.views.decorators.csrf import csrf_exempt
import json
import os 
import base64


@csrf_exempt
def paint(request):
    if request.method == 'GET':
        return render(request, 'paint.html')
    elif request.method == 'POST':
        filename = request.POST['save_fname']
        data = request.POST['save_cdata']
        image = request.POST['save_image']
        file_data = Files(name=filename, image=data, canvas_image=image)

        filename_2 = filename + "_2";
        local_file_2 = open(os.path.join("/home/laptop/Desktop/", filename_2) ,"wb")
        local_file_2.write(file_data.canvas_image[22:]);
        local_file_2.close();

        image = open( os.path.join("/home/laptop/Desktop/", filename+".png" ), "wb")
        image.write(file_data.canvas_image[22:].decode('base64'))
        image.close()


        file_data.save()
        return HttpResponseRedirect('/')
 
@csrf_exempt       
def files(request):
    if request.method == 'GET':
        all_data = Files.objects.all()
        return render(request, 'files.html', { 'files': all_data })

def search(request):
    if 'filename' in request.GET:
        filename = request.GET['filename']
        datafile = Files.objects.get(name=filename)
        return render(request, 'search.html', { 'data': datafile.canvas_image, 'filename': filename })
    
