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


class Product(models.Model):
    category = models.ForeignKey('Category', null=False, blank=False, on_delete=models.CASCADE)
    design = models.ForeignKey('Design', null=False, blank=False, on_delete=models.CASCADE)
    template_link = models.URLField(
        max_length=256,
        db_index=True,
        unique=True,
        blank=True
    )
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    main_image_url = models.URLField(max_length=1024, null=True, blank=True)
    main_image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

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


class ProductOptions(models.Model):
    product = models.ForeignKey('Product', null=False, blank=False, on_delete=models.CASCADE)
    article_nr = models.CharField(max_length=15, validators=[MinLengthValidator(15)], unique=True, null=False, blank=False)
    size = models.ForeignKey('Size', null=False, blank=False, on_delete=models.CASCADE)
    color = models.ForeignKey('Color', null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Product Options'


class ProductImages(models.Model):
    article = models.ForeignKey('ProductOptions', null=False, blank=False, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
