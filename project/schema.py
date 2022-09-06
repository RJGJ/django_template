'''
This is the main shema for the project
'''

from graphene_django import DjangoObjectType
from cms.schema import CMSQuery
import graphene


class Query(
    CMSQuery,
    graphene.ObjectType
):
    hello = graphene.String(default_value='Hi!')


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
