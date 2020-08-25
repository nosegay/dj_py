from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(
        request,
        'home.html'
    )


def signup(request):
    context = {}

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')

        context['form'] = form
    else:
        context['form'] = UserCreationForm()

    return render(
        request,
        'signup.html',
        context
    )
