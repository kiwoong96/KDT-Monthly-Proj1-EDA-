from django.shortcuts import render, HttpResponse

# Create your views here.
def domain(request):
    return render(request,'main.html',{})
    
def EDA(request):
    return render(request,'EDA.html',{})