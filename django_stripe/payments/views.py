import stripe
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Item


def get_item_view(request: HttpRequest, id: int) -> HttpResponse:
    """Render the main page to buy an Item."""
    item = get_object_or_404(Item, id=id)
    return render(request, "items.html", {"item": item})


def create_checkout_session_view(
    request: HttpRequest, id: int
) -> JsonResponse:
    """Create a Stripe checkout session and return the session id."""
    item = get_object_or_404(Item, id=id)
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{"price": item.stripe_price_id, "quantity": 1}],
        mode="payment",
        success_url=request.build_absolute_uri(reverse("success")),
        cancel_url=request.build_absolute_uri(reverse("cancel")),
    )
    return JsonResponse({"session_id": session.id})


def get_successful_page_view(request: HttpRequest) -> HttpResponse:
    """Render the successful payment template."""
    return render(request, "success.html")


def get_cancelled_page_view(request: HttpRequest) -> HttpResponse:
    """Render the cancelled payment template."""
    return render(request, "cancel.html")
