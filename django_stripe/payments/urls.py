from django.urls import path

from .views import (
    create_checkout_session_view,
    get_cancelled_page_view,
    get_item_view,
    get_successful_page_view,
)


urlpatterns = [
    path("item/<int:id>/", get_item_view, name="items"),
    path("buy/<int:id>/", create_checkout_session_view, name="buy_item"),
    path("success/", get_successful_page_view, name="success"),
    path("cancel/", get_cancelled_page_view, name="cancel"),
]
