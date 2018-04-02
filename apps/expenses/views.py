from django.shortcuts import render, redirect
import json
from apps.expenses.models import *
import datetime
import string
import random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def add_purchase(request):

    context = {'user': "test", 'data_base': "Plutus"}

    # return render(request, 'expenses/add_purchase.html', context)
    return render(request, 'expenses/add_purchase.html', context)


def add_purchase_processor(request):

    purchase_document = request.POST['purchase_document']
    purchase_dict = json.loads(purchase_document)

    currency = purchase_dict['currency']
    item_objects = []
    for item in purchase_dict['items']:
        item_object = Item(name=item['name'],
                           size=Size(value=item['size'], unit=item['unit']),
                           cost=Cost(value=item['cost'], currency=currency),
                           asset=item['asset'],
                           tags=item['tags'],
                           notes=item['notes'])
        amount = int(item['amount'])
        if amount > 1:
            ref = id_generator()
            item_object.notes = "%s: %s" % (ref, item_object.notes)
            for _ in range(amount):
                item_objects.append(item_object)
        else:
            item_objects.append(item_object)
    purchase_object = Purchase(
        items=item_objects,
        merchant=purchase_dict['merchant'],
        timestamp=datetime.datetime.strptime(purchase_dict['timestamp'], "%Y-%m-%d %H:%M"),
        discount=Cost(value=purchase_dict['discount'], currency=currency),
        cost=Cost(value=purchase_dict['total_cost'], currency=currency),
        charges=Cost(value=purchase_dict['charges'], currency=currency),
        tags=purchase_dict['purchase_tags']
    )

    # print(purchase_object)
    purchase_object.save()

    return redirect("/")
