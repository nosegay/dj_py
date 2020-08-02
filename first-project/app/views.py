from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
from pathlib import Path


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.today()
    msg = f'Текущее время: {current_time.strftime("%H:%M:%S")}'
    return HttpResponse(msg)


def workdir_view(request):
    work_dir = Path.cwd()
    file_list = f'Список файлов в рабочей директории: {", ".join([_file.name for _file in work_dir.glob("*")])}'
    return HttpResponse(file_list)
