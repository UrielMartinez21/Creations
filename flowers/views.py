from django.shortcuts import render

# Create your views here.
def yellow_flowers(request):
    # Get the user's name from the URL
    name = request.GET.get('name', '')

    return render(request, 'flowers/yellow_flowers.html', {'name': name})