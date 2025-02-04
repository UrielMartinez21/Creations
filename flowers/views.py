from django.shortcuts import render

# Create your views here.
def yellow_flowers(request):
    return render(request, 'flowers/yellow_flowers.html')