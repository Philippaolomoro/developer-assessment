import graphene

import product.queries


class Query(product.queries.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
