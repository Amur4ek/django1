import datetime
from os import listdir
from django.shortcuts import render, reverse
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {'pages': pages}
    return render(request, template_name, context)

def time(request):
    return HttpResponse(f'current_time = {datetime.datetime.now().time()}')

def workdir(request):
    return HttpResponse(f'workdir = {listdir()}')


