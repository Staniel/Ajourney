from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	context = {'test': 1}
	return render(request, 'travelplans/index.html', context)
