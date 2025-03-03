from typing import Any

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Item


@receiver(post_save, sender=Item)
def create_stripe_product_signal(
    sender: Item, instance: Item, created: bool, **kwargs: Any
):
    """Catch a signal after saving an Item instance to create it in Stripe."""
    if created:
        instance.create_stripe_product()
