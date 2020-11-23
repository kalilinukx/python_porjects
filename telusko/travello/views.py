from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"index.html",{'price':700})
def index(request):
    return render(request, "index.html")