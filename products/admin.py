from django.contrib import admin
from nested_inline.admin import (
    NestedModelAdmin,
    NestedStackedInline,
    NestedTabularInline)
from .models import (
    Category,
    ProductGroup,
    ProductDesignGroup,
    DesignCategory,
    Design,
    Size,
    Color,
    Product,
    ProductOptions,
    ProductImages,
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


class DesignAdmin(NestedTabularInline):
    model = Design
    readonly_fields = (
        'name',
    )
    list_display = (
        'display_name',
        'name',
    )


class DesignCategoryAdmin(NestedStackedInline):
    model = DesignCategory
    inlines = [DesignAdmin, ]
    readonly_fields = ('name', )
    list_display = (
        'display_name',
        'name',
    )


class ProductDesignGroupAdmin(NestedModelAdmin):
    readonly_fields = ('name', )
    inlines = [DesignCategoryAdmin, ]
    list_display = (
        'display_name',
        'name',
    )


class SizeAdmin(admin.ModelAdmin):
    readonly_fields = ('name', )
    list_display = (
        'display_name',
        'name',
        'relative_size',
    )


class ColorAdmin(admin.ModelAdmin):
    readonly_fields = ('name', )
    list_display = (
        'display_name',
        'name',
        'hex_code',
        'rgb_code',
    )


class ProductImagesAdmin(NestedTabularInline):
    model = ProductImages
    list_display = (
        'article',
        'main_image_url',
    )


class ProductOptionsAdmin(NestedStackedInline):
    model = ProductOptions
    inlines = [ProductImagesAdmin, ]
    list_display = (
        'product',
        'size',
        'color',
    )


class ProductAdmin(NestedModelAdmin):
    readonly_fields = ('name', )
    inlines = [ProductOptionsAdmin, ]
    list_display = (
        'category',
        'design',
        'template_link',
        'display_name',
        )

    def template_link_admin(self, obj):
        if obj.template_link:
            return "<a href='%s'>Link</a>" % obj.template_link
        else:
            return ''


admin.site.register(ProductGroup, ProductGroupAdmin)
admin.site.register(ProductDesignGroup, ProductDesignGroupAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Product, ProductAdmin)
