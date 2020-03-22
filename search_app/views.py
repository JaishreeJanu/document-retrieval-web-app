from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import DocumentForm
from .inverted_index import Inverted as iv
import os
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json
from django.template import Context, Template

# Create your views here.
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        # Whenever a new document is being added, inverted index module is called
        path = os.getcwd() + '/documents/'
        files = os.listdir(path)
        for filename in files:
            print(filename)
            text = iv.readfile(path, filename)
            text = iv.preprocess(text)
            iv.create_index(text, filename)
        return redirect('model_form_upload')
    else:
        form = DocumentForm()
    return render(request, 'file_upload_form.html', {
        'form': form
    })

@csrf_exempt
@api_view(['POST'])
def search_query(request):
    data = request.data
    query = iv.preprocess(data["term"]) #preprocess query
    results = iv.search(query)
    if not results:
        print("No document found for your query")
        return redirect('model_form_upload')
    else:
        print(results)
        return render(request,'file_upload_form.html',{"results": results})
