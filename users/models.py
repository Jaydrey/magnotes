from uuid import uuid4
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email: str = None, password: str = None, **extra_fields):
        if email is None:
            raise ValueError({"error": _("Email field is required")})
        if password is None:
            raise ValueError({"error": _("Password field is required")})

        email = self.normalize_email(email)
        try:
            user: User = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user
        except Exception as e:
            print(f"Error while creating user {e}")
            return None

    def create_superuser(self, email: str = None, password: str = None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        default_related_name = _("users")
        indexes = (
            models.Index(fields=("id",)),
        )
        ordering = ("-created_at",)
        verbose_name = _("user")
        verbose_name_plural = _("users")

    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    email = models.EmailField(_("email"), unique=True)
    first_name = models.CharField(_("first name"), max_length=50, null=True)
    last_name = models.CharField(_("last name"), max_length=50, null=True)
    is_active = models.BooleanField(_("is active"), default=True)
    is_superuser = models.BooleanField(("is super user"), default=False)
    is_staff = models.BooleanField(_("is staff"), default=False)
    is_deleted = models.BooleanField(_("is deleted"), default=False)
    created_at = models.DateTimeField(
        _("created at"), default=timezone.now, editable=False)
    updated_at = models.DateTimeField(
        _("updated at"), editable=False, null=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    objects = UserManager()

    def __str__(self) -> str:
        return f"{_(self.email)}"
