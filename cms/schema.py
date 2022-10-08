from graphene_django import DjangoObjectType
from .models import MetaData, Page
import graphene


class MetaDataType(DjangoObjectType):
    class Meta:
        model = MetaData
        fields = ('id', 'title', 'description')


class MetaDataMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String(required=True)
        description = graphene.String(required=True)

    metadata = graphene.Field(MetaDataType)

    @classmethod
    def mutate(self, root, info, title, description):
        metadata = MetaData(
            title=title,
            description=description
        )
        metadata.save()
        return MetaDataMutation(metadata=metadata)


class CMSQuery(graphene.ObjectType):
    list_metadata = graphene.List(MetaDataType)
    metadata_by_id = graphene.Field(MetaDataType, id=graphene.String())

    def resolve_all_metadata(self, info):
        return MetaData.objects.all()


class CMSMutation(graphene.ObjectType):
    create_metadata = MetaDataMutation.Field()
