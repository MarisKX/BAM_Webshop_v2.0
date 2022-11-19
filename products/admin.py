from django.contrib import admin
from nested_inline.admin import (
    NestedModelAdmin,
    NestedStackedInline,
    NestedTabularInline)
from .models import (
    Category,
    ProductGroup,
)


class CategoryAdmin(admin.TabularInline):
    model = Category
    readonly_fields = ('name', )
    list_display = (
        'product_group',
        'display_name',
        'name',
    )


class ProductGroupAdmin(admin.ModelAdmin):
    inlines = (CategoryAdmin,)
    readonly_fields = ('name', )
    list_display = (
        'display_name',
        'name',
    )


admin.site.register(ProductGroup, ProductGroupAdmin)