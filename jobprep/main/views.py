from django.shortcuts import render
from .models import Exam, Resource
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'index.html')

def higher_studies(request):
    exams = Exam.objects.all()
    resources = Resource.objects.all()
    return render(request, 'higher_studies.html', {'exams': exams, 'resource' : resources})

def login(request):
    return HttpResponse("hello login")

def signup(request):
    return HttpResponse("hello signup")