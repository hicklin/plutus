from django.shortcuts import render, redirect


def menu(request):

    context = {'user': "test", 'data_base': "Plutus"}

    return render(request, 'main/menu.html', context)


def index(request):

    context = {'user': "test", 'data_base': "Plutus"}

    return render(request, 'main/index.html', context)


def not_found(request):

    context = {'user': "test", 'data_base': "Plutus"}

    return render(request, 'main/404.html', context)
