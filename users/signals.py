from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver

from .models import User
from accounts.models import Account


@receiver(signal=post_save, sender=User)
def user_created(sender: User, instance: User, created: bool, **kwargs):
    if created:
        try:
            account = Account.objects.create(
                user=instance,
            )
            return account
        except Exception as e:
            instance.delete()
            instance.save()
            return None

