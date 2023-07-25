from uuid import uuid4
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _

from notes.models import Note


class Tag(models.Model):
    class Meta:
        default_related_name = _("tags")
        indexes = (
            models.Index(fields=("id", "name")),
        )
        ordering = ("name",)
        unique_together = ("name", "note",)
        verbose_name = _("tag")
        verbose_name_plural = _("tags")

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(_("name"), max_length=100,)
    note = models.ForeignKey(
        Note, verbose_name=_("note"), on_delete=models.SET_NULL, null=True)
    is_deleted = models.BooleanField(_("is deleted"), default=False)
    created_at = models.DateTimeField(
        _("created at"), default=timezone.now, editable=False)
    updated_at = models.DateTimeField(_("updated at"), null=True)

    def __str__(self) -> str:
        return f"{self.name}"
