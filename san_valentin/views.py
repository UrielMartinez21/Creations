from django.shortcuts import render


def main_index(request):
    return render(request, 'main_index.html')


def index_v1(request):
    return render(request, 'index_v1.html')