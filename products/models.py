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


class ProductDesignGroup(models.Model):
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Design Groups and Categories'

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


class DesignCategory(models.Model):
    product_design_group = models.ForeignKey(ProductDesignGroup, null=True, blank=False, on_delete=models.CASCADE, related_name='product_design_group_for_category')
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Design Categories'

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


class Design(models.Model):
    product_design_category = models.ForeignKey(DesignCategory, null=True, blank=False, on_delete=models.CASCADE, related_name='product_design_category')
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Design Templates'

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


class Size(models.Model):
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)
    relative_size = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Product Sizes'

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


class Color(models.Model):
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)
    hex_code = models.CharField(max_length=7, validators=[MinLengthValidator(7)], unique=True, null=False, blank=False)
    rgb_code = models.CharField(max_length=11, validators=[MinLengthValidator(5)], unique=True, null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Product Colors'

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