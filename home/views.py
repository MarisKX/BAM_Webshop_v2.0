from django.shortcuts import render
from products.models import (
    Category,
    ProductGroup,
    ProductDesignGroup,
    DesignCategory,
    Design
)


def index(request):
    all_product_design_groups = ProductDesignGroup.objects.all().order_by('display_name', )
    all_designs = Design.objects.all().order_by('display_name', )
    all_product_groups = ProductGroup.objects.all().order_by('display_name', )

    context = {
        'all_product_design_groups': all_product_design_groups,
        'all_designs': all_designs,
    }

    return render(request, 'home/index.html', context)
