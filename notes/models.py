from uuid import uuid4
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import Account


class Note(models.Model):
    class Meta:
        default_related_name = _("notes")
        indexes = (
            models.Index(fields=("id", "header")),
        )
        ordering = ("updated_at", "created_at")
        verbose_name = _("note")
        verbose_name_plural = _("notes")

    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    header = models.CharField(_("header"), max_length=250, null=True)
    body = models.TextField(_("body"), null=False, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(_("is deleted"), default=False)
    created_at = models.DateTimeField(
        _("created at"), default=timezone.now, editable=False)
    updated_at = models.DateTimeField(_("updated at"), null=True)

    def __str__(self) -> str:
        return f"{self.header}"
