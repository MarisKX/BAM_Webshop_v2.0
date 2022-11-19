from django.db import models
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
    MinLengthValidator,
)


class ProductGroup(models.Model):
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Product Groups and Categories'

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the name.
        """
        self.name = self.display_name.replace(" ", "_").lower()
        super().save(*args, **kwargs)


class Category(models.Model):
    product_group = models.ForeignKey(ProductGroup, null=True, blank=False, on_delete=models.CASCADE, related_name='product_group')
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the name.
        """
        self.name = self.display_name.replace(" ", "_").lower()
        super().save(*args, **kwargs)