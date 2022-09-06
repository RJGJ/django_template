from graphene_django import DjangoObjectType
from cms.models import MetaData, Page
import graphene


class MetaDataType(DjangoObjectType):
    class Meta:
        model = MetaData
        fields = ('id', 'title', 'description')


class Query(graphene.ObjectType):
    all_metadata = graphene.List(MetaDataType)

    def resolve_all_metadata(self, info):
        return MetaData.objects.all()
