from django.db import models
from django.contrib.auth.models import User
from store.models import Product


class CartItem(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField(
        default=1
    )


    def subtotal(self):

        return self.product.price * self.quantity


    def __str__(self):

        return self.product.name