from mongoengine import *


class Cost(EmbeddedDocument):
    value = FloatField()
    currency = StringField(max_length=3, default='GBP')


class Size(EmbeddedDocument):
    value = FloatField()
    unit = StringField(max_length=10)


class Item(EmbeddedDocument):
    name = StringField(max_length=200)
    size = EmbeddedDocumentField(Size)
    cost = EmbeddedDocumentField(Cost)
    asset = BooleanField()
    tags = ListField(StringField(max_length=30), null=True)
    notes = StringField(null=True)


# class Merchant(EmbeddedDocument):
#     name = StringField(max_length=100)
#     location = StringField(max_length=100)
#     post_code = StringField(max_length=10)


class Charges(EmbeddedDocument):
    note = StringField()
    cost = ListField(EmbeddedDocumentField(Cost))


class Purchase(Document):
    items = ListField(EmbeddedDocumentField(Item))
    # merchant = EmbeddedDocumentField(Merchant)
    merchant = StringField()
    timestamp = DateTimeField()
    discount = EmbeddedDocumentField(Cost, null=True)
    cost = EmbeddedDocumentField(Cost, null=True)
    charges = EmbeddedDocumentField(Cost, null=True)
    tags = ListField(StringField(max_length=30), null=True)


class ItemTags(Document):
    name = StringField(max_length=15)
    description = StringField()


class PurchaseTags(Document):
    name = StringField(max_length=15)
    description = StringField()


class Units(Document):
    unit = StringField(max_length=15)
    description = StringField()
