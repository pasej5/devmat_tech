from django.shortcuts import render

from django.shortcuts import render

def index(request):
    return render(request, 'landing_page/index.html')

def about(request):
    return render(request, 'landing_page/about.html')

def blog(request):
    return render(request, 'landing_page/medium.html')

def contact(request):
    return render(request, 'landing_page/contact.html')

def portfolio(request):
    return render(request, 'landing_page/portfolio.html')
