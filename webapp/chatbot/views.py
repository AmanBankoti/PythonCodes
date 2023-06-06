from django.shortcuts import render
# Create your views here.

def b(request):
    return render(request ,'chatbot/index.html')
