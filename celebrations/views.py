from django.shortcuts import render
import user_agents


def yellow_flowers(request):
    name = request.GET.get('name', '')
    return render(request, 'flowers/yellow_flowers.html', {'name': name})


def valentine_v1(request):
    name = request.GET.get('name', '')
    return render(request, 'valentine/v1.html', {'name': name})


def dentist(request):
    name = request.GET.get('name', '')
    return render(request, 'dentist/v1.html', {'name': name})