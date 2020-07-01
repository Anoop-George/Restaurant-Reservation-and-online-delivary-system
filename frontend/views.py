from django.shortcuts import render



def index(request):
    return render(request, 'frontend/index_react.html')


def main(request):
    return render(request, 'frontend/index.html')