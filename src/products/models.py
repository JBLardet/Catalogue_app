from django.db import models


# Todo: Figure out how to link to special offers.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Catégorie"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=80, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    description = models.CharField(max_length=255)
    price = models.FloatField(max_length=6)

    #     TODO: anything to add here to find the correct image ?

    # TODO: tenir compte de la promotion dans le prix
    # @property
    # def price_on_sales(self):
        # retourner le prix final en prenant self.price et lui appliquant la remise stockée dans la classe pour promotions, si:
        # 1. Une telle promotion existe (mettre en place un système pour vérifier l'existence de la promotion)
        # 2. Une telle promotion est toujours en vigueur (mieux vaut gérer ça hors de cette propriété pour éviter de vérifier la validité de la promotion à chaque appel de chaque produit)

    class Meta:
        verbose_name = "Produit"

    def __str__(self):
        return self.name
