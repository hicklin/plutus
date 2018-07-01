from apps.expenses.models import Purchase, Item


def get_items(**kwargs):

    purchases = Purchase.objects.filter(**kwargs)
    return purchases
