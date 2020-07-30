from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def Home(requset):
    return render(requset, 'QANeiApp/Index.html')


def Login(requset):
    return render(requset, 'QANeiApp/login.html')


def CreateProblem(requset):
    return render(requset, 'QANeiApp/dashboard.html')


def SolveProblem(requset):
    return render(requset, 'QANeiApp/index.html')
