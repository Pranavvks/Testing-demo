import graphene
from graphene_django import DjangoObjectType
from .models import Person

class PersonType(DjangoObjectType):
    class Meta:
        model = Person
        fields = ('name', 'content')
        
        
class Query(graphene.ObjectType):
    person = graphene.Field(PersonType, name=graphene.String())
    
    
    def resolve_person(self, info, **kwargs):
        name = kwargs.get('name')
        return Person.objects.get(name=name)
        