from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.name}"


class OrderDetail(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.item.name} - {self.amount}"

    def order_price(self):
        return self.item.price * self.amount


class Order(models.Model):
    items = models.ManyToManyField(OrderDetail)

    def __str__(self) -> str:
        items = [f"{item.item.name}({item.amount}pcs)" for item in self.items.all()]
        return ", ".join(items)

    def total_price(self):
        return sum([item.item.price * item.amount for item in self.items.all()])
