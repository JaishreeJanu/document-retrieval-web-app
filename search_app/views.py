from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import DocumentForm

# Create your views here.
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('model_form_upload')
    else:
        form = DocumentForm()
    return render(request, 'file_upload_form.html', {
        'form': form
    })
