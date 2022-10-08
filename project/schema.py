'''
This is the main schema for the project
'''

from graphene_django import DjangoObjectType
from cms.schema import CMSQuery, CMSMutation
import graphene


class Query(
    CMSQuery,
    graphene.ObjectType
):
    hello = graphene.String(default_value='Hi!')


class Mutation(
    CMSMutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
