from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Restaurant
from datetime import datetime

def index(request):
    return render(request,"food_inspectre/index.html")

def loadJSON(request):
	if request.method == "POST":
		print('Raw Data: "%s"' % request.body)
	return redirect('/')
