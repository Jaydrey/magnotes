import graphene
from graphene_django.filter import DjangoFilterConnectionField

# filters
from users.filters import UserFilter

# object type
from users.types import (
    UsersType,
    UserType,
    ProfileType
)

# mutations
from users.mutations import CreateUserMutation

# models
from accounts.models import Account
from users.models import User


class Mutation(graphene.ObjectType):
    create_user = CreateUserMutation.Field()


class Query(graphene.ObjectType):
    profile = graphene.Field(
        ProfileType, user_id=graphene.String(required=True))
    users = DjangoFilterConnectionField(UsersType, filterset_class=UserFilter)
    user = graphene.Field(UserType, user_id=graphene.String(required=True))

    def resolve_profile(root, info, user_id):
        if not user_id:
            return None
        try:
            user: User = User.objects.get(id=user_id)
            if user.is_deleted:
                return None

            full_name: str = f"{user.first_name} {user.last_name}"
            account: Account = user.accounts
            notes_len = len(account.notes.all())
            return ProfileType(
                full_name=full_name,
                email=user.email,
                avatar=None,
                notes_number=notes_len,
            )
        except Exception as error:
            print(error)
            return None

    def resolve_user(root, info, user_id):
        try:
            new_user: User = User.objects.get(id=user_id)
            if new_user.is_deleted or new_user.is_active == False:
                return None
            return new_user
        except Exception as error:
            return None


schema = graphene.Schema(query=Query, mutation=Mutation)
