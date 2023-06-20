from django.shortcuts import render
from .models import Student
from .resources import StudentResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse

from .forms import StudentForm

# Create your views here.

def uploadFile(request):
    if request.method == 'POST':
        studentResource = StudentResource()
        dataset = Dataset()
        newStudent = request.FILES['myfile']

        if not newStudent.name.endswith('xlsx'):
            messages.info(request, 'Wrong format')
            return render(request, 'file.html')
        
        loadedData = dataset.load(newStudent.read(), format='xlsx')
        for data in loadedData:
            value = Student(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7]
            )
            value.save()
    return render(request, 'file.html')

def uploadForm(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            form = StudentForm()
    context = {'form': form}
    return render(request, 'form.html', context)


def uploadHome(request):

    return render(request, 'home.html')
