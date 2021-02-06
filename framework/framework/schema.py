import graphene
from user.schema import Query as PersonQuery

class Query( PersonQuery):
    pass


schema = graphene.Schema(query=Query)