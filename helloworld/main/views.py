from django.shortcuts import render
import datetime

# Create your views here.
def index(request, page=0):
	return render(request,'polls/index.html', {'data':page})
