from datetime import datetime
from time import ctime
from django.shortcuts import render
from django.conf import settings
from pathlib import Path


def file_list(request, date=None):
    template_name = 'index.html'

    if date is not None:
        files = filter(lambda x: datetime.strptime(ctime(x.stat().st_mtime), '%c') <= date,
                       Path(settings.FILES_PATH).glob('*.*'))
    else:
        files = Path(settings.FILES_PATH).glob('*.*')

    files_info = [dict(name=_file.name,
                       ctime=datetime.strptime(ctime(_file.stat().st_ctime), '%c'),
                       mtime=datetime.strptime(ctime(_file.stat().st_mtime), '%c'))
                  for _file in files]
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    context = {
        'files': files_info,
        'date': date  # Этот параметр необязательный
    }

    return render(request, template_name, context)


def file_content(request, name):
    _file = Path(settings.FILES_PATH).joinpath(name)
    return render(
        request,
        'file_content.html',
        context={'file_name': _file.name, 'file_content': _file.read_text()}
    )

