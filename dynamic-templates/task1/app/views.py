from django.shortcuts import render
import csv
from pprint import pprint

def inflation_view(request):
    template_name = 'inflation.html'

    with open(r'inflation_russia.csv', 'r', encoding='utf-8') as fp:
        csv_data = csv.DictReader(fp, delimiter=';', restval='-')
        headers = csv_data.fieldnames
        content = list(csv_data)

    return render(request, template_name, context={'headers': headers, 'content': content})
