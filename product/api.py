from ninja import Router

from . import schema
from core.schema import error_schema_dict, handle_exception

from .models import Product

from typing import List


product_router = Router(tags=["Product API"])


@product_router.get(
    '/', 
    response={200: List[schema.ProductSchema], **error_schema_dict}, 
    summary="Product List", 
    auth=None
)
def product_list(request):
    try:
        products = Product.objects.all().order_by("-created_date")
        return products

    except Exception as e:
        return handle_exception(e)


@product_router.get(
    '/{product_id}/', 
    response={200: schema.ProductSchema, **error_schema_dict}, 
    summary="Product Item", 
    auth=None
)
def product(request, product_id: int):
    try:
        product = Product.objects.get(id=product_id)
        return product
    
    except Exception as e:
        return handle_exception(e)
