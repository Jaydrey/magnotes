import graphene
from graphene import Mutation, ObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from .types import UsersType

from .serializers import CreateUserSerializer
from .models import User


class CreateUserMutation(SerializerMutation):
    class Meta:
        serializer_class = CreateUserSerializer
        model_operations = ("create",)

