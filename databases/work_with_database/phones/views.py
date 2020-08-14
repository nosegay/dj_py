from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'

    sort_param = request.GET.get('sort')
    if sort_param == 'name':
        context = {"phones_info": Phone.objects.order_by('name')}
    elif sort_param == 'min_price':
        context = {"phones_info": Phone.objects.order_by('price')}
    elif sort_param == 'max_price':
        context = {"phones_info": Phone.objects.order_by('-price')}
    else:
        context = {"phones_info": Phone.objects.all()}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {"phone_info": Phone.objects.get(slug=slug)}
    return render(request, template, context)
