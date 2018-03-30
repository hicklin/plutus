from django.shortcuts import render, redirect


def add_purchase(request):

    context = {'user': "test", 'data_base': "Plutus"}

    return render(request, 'expenses/add_purchase.html', context)


def add_purchase_processor(request):

    return redirect("/")
