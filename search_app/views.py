from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import DocumentForm
from .inverted_index import Inverted as iv
import os

# Create your views here.
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('model_form_upload')
    else:
        form = DocumentForm()
        path = os.getcwd() + '/documents/'
        files = os.listdir(path)
        for filename in files:
            text = iv.readfile(path, filename)
            text = iv.preprocess(text) 
            iv.create_index(text, filename)
    return render(request, 'file_upload_form.html', {
        'form': form
    })
