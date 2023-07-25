from uuid import uuid4
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from users.models import User


class Account(models.Model):
    class Meta:
        default_related_name = _("accounts")
        indexes = (
            models.Index(fields=("id",)),
        )
        ordering = ("id",)
        verbose_name = _("account")
        verbose_name_plural = _("accounts")

    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    name = models.CharField(_("name"), max_length=100, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id}"

    def __repr__(self) -> str:
        return f"{self.__class__.name}(name={_(self.name)}, user={self.user.email})"
