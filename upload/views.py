from django.shortcuts import render
from .forms import Student_form
from django.http import HttpResponse
from upload.functions import file_upload
from .models import Save_model
# Create your views here.

def demo(request):
	if request.method == 'POST':
		form = Student_form(request.POST,request.FILES)

		if form.is_valid():
			file_upload(request.FILES['file'])
			return HttpResponse("File uploaded Successfully")
	else:
		form = Student_form()
		return render(request,'file.html',{'form':form})

def save(request):
	if request.method == 'POST':
		form = Student_form(request.POST,request.FILES)

		if form.is_valid():
			save = Save_model()
			save.firstname = form.cleaned_data['firstname']
			save.lastname = form.cleaned_data['lastname']
			save.file = form.cleaned_data['file']
			save.save()

			return HttpResponse('File uploaded Successfully')
	else:
		form = Student_form()
		return render(request,'file.html',{'form':form})


