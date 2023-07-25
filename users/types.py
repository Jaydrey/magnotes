import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType


from .models import User, UserManager


class UsersType(DjangoObjectType):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "last_login",
        )
        interfaces = (relay.Node,)
    user_id = graphene.UUID(source="id")

    @classmethod
    def get_queryset(cls, queryset: UserManager, info):
        if info.context.user.is_anonymous:
            return queryset.filter(is_staff=False)
        return queryset


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "is_active",
            "last_login",
            "updated_at",
            "last_login",
        )


class ProfileType(ObjectType):
    full_name = graphene.String()
    email = graphene.String()
    avatar = graphene.String()
    notes_number = graphene.Int()
