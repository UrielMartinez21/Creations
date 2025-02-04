from django.shortcuts import render


def main_index(request):
    return render(request, 'san_valentin/main_index.html')


def index_v1(request):
    return render(request, 'san_valentin/index_v1.html')