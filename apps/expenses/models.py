from mongoengine import *


class Cost(EmbeddedDocument):
    value = FloatField()
    currency = StringField(max_length=3, default='GPB')


class Quantity(EmbeddedDocument):
    value = FloatField()
    unit = StringField(max_length=10)


class Item(EmbeddedDocument):
    name = StringField(max_length=200)
    quantity = ListField(EmbeddedDocumentField(Quantity))
    cost = ListField(EmbeddedDocumentField(Cost))
    asset = BooleanField()
    tags = ListField(StringField(max_length=30))


class Merchant(EmbeddedDocument):
    name = StringField(max_length=100)
    location = StringField(max_length=100)
    post_code = StringField(max_length=10)


class Charges(EmbeddedDocument):
    note = StringField()
    cost = ListField(EmbeddedDocumentField(Cost))


class Purchase(Document):
    items = ListField(EmbeddedDocumentField(Item))
    merchant = ListField(EmbeddedDocumentField(Merchant))
    timestamp = DateTimeField()
    discount = ListField(EmbeddedDocumentField(Cost))
    cost = ListField(EmbeddedDocumentField(Cost))
    extra_charges = ListField(EmbeddedDocumentField(Charges))
    tags = ListField(StringField(max_length=30))

