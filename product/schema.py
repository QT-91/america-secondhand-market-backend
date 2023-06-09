from ninja import ModelSchema
from core.schema import ImageSchema

from .models import Product, ProductImage
from typing import List


class ProductImageSchema(ModelSchema):
    image: ImageSchema = None
    
    class Config:
        model = ProductImage
        model_fields = ['id', 'image']


class ProductSchema(ModelSchema):
    images: List[ProductImageSchema] = []

    class Config:
        model = Product
        model_fields = [
            'id',
            'title',
            'description',
            'price',
            'negotiable',
            'category',
            'seller_info',
            'location',
            'created_date',
            'status',
        ]
