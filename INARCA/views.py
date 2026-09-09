from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    print(request.user)
    return HttpResponse("Welcome to the INARCA home page!")