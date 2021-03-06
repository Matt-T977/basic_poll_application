from django import http
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, World. You're at the polls index!")

def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")

def result(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")

