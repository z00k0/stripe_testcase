from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView, ListView
from django.conf import settings
import stripe
from stripetest.models import Item, Order


stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


class ItemListView(ListView):
    model = Item
    template_name = "items.html"
    queryset = Item.objects.all()


class BuyView(View):
    def get(self, request, id):
        item = get_object_or_404(Item, pk=id)
        name = item.name
        price = int(item.price * 100)
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[
                    {
                        "price_data": {
                            "currency": "usd",
                            "product_data": {"name": name},
                            "unit_amount": price,
                        },
                        "quantity": 1,
                    }
                ],
                mode="payment",
                success_url="http://127.0.0.1:8080/success",
                cancel_url="http://127.0.0.1:8080/cancel",
            )
        except Exception as e:
            return str(e)
        return JsonResponse({"id": session.id})


class ItemView(TemplateView):
    template_name = "item.html"

    def get_context_data(self, **kwargs):
        item = get_object_or_404(Item, pk=kwargs["id"])
        print(f"{item=}")
        context = super(ItemView, self).get_context_data(**kwargs)
        context.update(
            {
                "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
                "item": item,
            }
        )
        return context


class OrderListView(ListView):
    model = Order
    template_name = "orders.html"
    queryset = Order.objects.all()


class BuyOrderView(View):
    def get(self, request, id):
        order = get_object_or_404(Order, pk=id)
        # name = order.name
        # price = int(item.price * 100)
        line_items = []
        print(f"{order=}")
        print(f"{order.items.all()=}")
        for item in order.items.all():
            quantity = item.amount
            name = item.item.name
            price = int(item.item.price * 100)
            line_items.append(
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {"name": name},
                        "unit_amount": price,
                    },
                    "quantity": quantity,
                }
            )

        try:
            session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=line_items,
                mode="payment",
                success_url="http://127.0.0.1:8080/success",
                cancel_url="http://127.0.0.1:8080/cancel",
            )
        except Exception as e:
            return str(e)
        return JsonResponse({"id": session.id})


class OrderView(TemplateView):
    template_name = "order.html"

    def get_context_data(self, **kwargs):
        order = get_object_or_404(Order, pk=kwargs["id"])
        print(f"{order=}")
        context = super(OrderView, self).get_context_data(**kwargs)
        context.update(
            {
                "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
                "order": order,
            }
        )
        return context
