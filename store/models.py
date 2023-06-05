from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone

from shop.settings import AUTH_USER_MODEL

"""

-NOM
-PRIX
-LA QUANTITE EN STOCK
-DESCRIPTION
-IMAGE

"""
class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.quantity})"

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})

# Article (Order)
"""
- Utilisateur
- Produit
- Quantite
- Commande ou non
"""

class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"


# Panier (Cart)
"""
- Utilisateur
- Articles
- Commande ou non
- Date de la commande
"""


class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)

    def __str__(self):
        return self.user.username

    def delete(self, *args, **kwargs):
        for order in self.orders.all():
            order.ordered = True
            order.ordered_date = timezone.now()
            order.save()

        self.orders.clear()
        super().delete(*args, **kwargs)


















