import stripe
from django.db import models


class Item(models.Model):
    """Describdes one item of a product."""

    name = models.CharField(
        verbose_name="Единица товара",
        max_length=255,
        unique=True,
        blank=False,
        null=False,
    )
    description = models.TextField(
        verbose_name="Описание товара",
        blank=False,
        null=False,
    )
    price = models.DecimalField(
        verbose_name="Цена товара",
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False,
    )
    stripe_price_id = models.CharField(
        verbose_name="ID товара в Stripe",
        max_length=255,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.name

    def create_stripe_product(self) -> None:
        """Create a product in Stripe if it's not existed."""
        if not self.stripe_price_id:
            product = stripe.Product.create(
                name=self.name, description=self.description
            )
            price = stripe.Price.create(
                unit_amount=int(self.price * 100),
                currency="usd",
                product=product.id,
            )
            self.stripe_price_id = price.id
            self.save()
