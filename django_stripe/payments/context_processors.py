from django.conf import settings
from django.http import HttpRequest


def get_stripe_public_key(request: HttpRequest) -> dict[str, str]:
    """Provide the public Stripe key to use in the templates."""
    return {"STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY}
