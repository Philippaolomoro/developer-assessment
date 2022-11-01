from graphene import relay
from graphene_django import DjangoObjectType

from product.models import Product


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        filter_fields = {
            "id": ['exact'], 
            "name": ['exact', 'icontains', 'istartswith'], 
            "description": ['exact', 'icontains'], 
            "sku": ['exact'], 
            "price": ['exact'], 
            "image": ['exact']
        }
        interfaces = (relay.Node,)