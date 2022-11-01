from graphene import ObjectType, relay
from graphene_django.filter import DjangoFilterConnectionField

from product.types import ProductType


class Query(ObjectType):
    product = relay.Node.Field(ProductType)
    all_products = DjangoFilterConnectionField(ProductType)
