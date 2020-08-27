from django.shortcuts import render
from django.http import HttpResponse

# Home index view
def index(request):
    return render(request, "index.html")
