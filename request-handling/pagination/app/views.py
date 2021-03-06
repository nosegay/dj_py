from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator

import csv
import urllib


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, 'r', encoding='cp1251') as fp:
        bus_info = list(csv.DictReader(fp))

    bus_station_pagi = Paginator(bus_info, 10)
    current_page = request.GET.get('page', 1)
    pagi_page = bus_station_pagi.get_page(current_page)

    if pagi_page.has_next():
        next_page = pagi_page.next_page_number()
        next_page_url = f"{reverse('bus_stations')}?{urllib.parse.urlencode({'page': next_page})}"
    else:
        next_page_url = None

    if pagi_page.has_previous():
        prev_page = pagi_page.previous_page_number()
        prev_page_url = f"{reverse('bus_stations')}?{urllib.parse.urlencode({'page': prev_page})}"
    else:
        prev_page_url = None

    return render_to_response('index.html', context={
        'bus_stations': pagi_page,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

