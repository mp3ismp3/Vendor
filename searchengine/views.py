from django.shortcuts import render


# Create your views here.
def homeview(request):
    return render(request, 'searchengine/home.html')
