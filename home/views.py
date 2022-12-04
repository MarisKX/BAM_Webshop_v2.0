from django.shortcuts import render
from django.http import JsonResponse
from products.models import (
    Category,
    ProductGroup,
    ProductDesignGroup,
    DesignCategory,
    Design
)


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def index(request):
    all_product_design_groups = ProductDesignGroup.objects.all().order_by('display_name', )
    all_designs = Design.objects.all().order_by('display_name', )
    all_product_groups = ProductGroup.objects.all()

    if is_ajax(request):
        product_group = request.GET.get('product_group')
        design_group = request.GET.get('design_group')
        if design_group is not None:
            print(design_group)
            design_categories = DesignCategory.objects.filter(product_design_group=design_group).values_list('display_name').order_by('name')
            return JsonResponse({"designs_to_return": list(design_categories)})
        elif product_group is not None:
            product_categories = Category.objects.filter(product_group=product_group).values_list('display_name').order_by('name')
            return JsonResponse({"categories_to_return": list(product_categories)})
            print(product_group)

    context = {
        'all_product_groups': all_product_groups,
        'all_product_design_groups': all_product_design_groups,
        'all_designs': all_designs,
    }

    return render(request, 'home/index.html', context)
