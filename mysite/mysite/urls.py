"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from stripetest.views import (
    BuyView,
    ItemView,
    SuccessView,
    CancelView,
    ItemListView,
    OrderView,
    OrderListView,
    BuyOrderView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("buy/<int:id>", BuyView.as_view(), name="buy"),
    path("item/<int:id>", ItemView.as_view(), name="item"),
    path("success/", SuccessView.as_view(), name="success"),
    path("cancel/", CancelView.as_view(), name="cancel"),
    path("items/", ItemListView.as_view(), name="items"),
    path("orders/", OrderListView.as_view(), name="orders"),
    path("order/<int:id>", OrderView.as_view(), name="order"),
    path("buy-order/<int:id>", BuyOrderView.as_view(), name="buy-order"),
]
