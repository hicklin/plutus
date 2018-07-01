from django.shortcuts import render, redirect
import json
from apps.expenses.models import *
import datetime
from ast import literal_eval
import string
import random
from distutils.util import strtobool

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def add_purchase(request):

    item_tags = [item_tag.name for item_tag in ItemTags.objects.all()]
    item_tags.sort()
    purchase_tags = [purchase_tag.name for purchase_tag in PurchaseTags.objects.all()]
    purchase_tags.sort()
    units = [unit.unit for unit in Units.objects.all()]
    merchants = ["%s %s" % (merchant.name, merchant.location) for merchant in Merchant.objects.all()]
    context = {"item_tags": item_tags, "purchase_tags": purchase_tags, "units": units, "merchants": merchants}

    # return render(request, 'expenses/add_purchase.html', context)
    return render(request, 'expenses/add_purchase.html', context)


def add_purchase_processor(request):

    purchase_document = request.POST['purchase_document']
    purchase_dict = json.loads(purchase_document)

    currency = purchase_dict['currency']
    item_objects = []
    for item in purchase_dict['items']:
        size = item['size']
        unit = item['unit']
        if size == "":
            size = None
        if unit == "":
            unit = None
        amount = int(item['amount'])
        if amount > 1:
            ref = id_generator()
            notes = "%s: %s" % (ref, item['notes'])
            for _ in range(amount):
                item_object = Item(name=item['name'],
                                   size=Size(value=size, unit=unit),
                                   cost=Cost(value=item['cost'], currency=currency),
                                   asset=bool(strtobool(str(item['asset']))),
                                   tags=item['tags'],
                                   notes=notes)
                saved_item_object = item_object.save()
                item_objects.append(saved_item_object)
        else:
            item_object = Item(name=item['name'],
                               size=Size(value=size, unit=unit),
                               cost=Cost(value=item['cost'], currency=currency),
                               asset=bool(strtobool(str(item['asset']))),
                               tags=item['tags'],
                               notes=item['notes'])
            saved_item_object = item_object.save()
            item_objects.append(saved_item_object)
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
