from django.shortcuts import render
# Create your views here.
def a(request):
    return render(request,'img_generator/index.html')
