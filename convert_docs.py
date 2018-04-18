import django
import os
import json
import datetime

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "plutus.settings")
    django.setup()

    from apps.expenses.models import Item, Purchase

    old_documents_filename = "plutus_purchase.json"

    purchases = json.load(open(old_documents_filename))

    for purchase in purchases:
        purchase_items = []
        for item in purchase['items']:
            try:
                tags = item['tags']
            except KeyError:
                tags = None
            new_item = Item(name=item['name'],
                            size=item['size'],
                            cost=item['cost'],
                            asset=item['asset'],
                            tags=tags,
                            notes=item['notes'])
            new_item.save()
            purchase_items.append(new_item)

        try:
            tags = purchase['tags']
        except KeyError:
            tags = None
        Purchase(items=purchase_items,
                 merchant=purchase['merchant'],
                 timestamp=datetime.datetime.strptime(purchase['timestamp']['$date'], "%Y-%m-%dT%H:%M:%S.000z"),
                 discount=purchase['discount'],
                 cost=purchase['cost'],
                 charges=purchase['charges'],
                 tags=tags).save()
