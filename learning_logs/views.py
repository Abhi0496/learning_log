from django.shortcuts import render

# Create your views here.

def index(request):
    """Home page for learning log"""
    return render(request, 'learning_logs/index.html')