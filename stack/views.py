from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name': 'Percy',
        'age': 26,
        'team': 'Everton FC'
    }
    return render(request, 'index.html', context)