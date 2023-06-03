from django.db import models
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
from wagtail.models import Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.search import index


class ProductImage(Orderable):
    product = ParentalKey(
        'Product', related_name='images', on_delete=models.CASCADE
    )
    image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, 
        related_name='+', on_delete=models.SET_NULL
    )
    panels = [
        FieldPanel('image'),
    ]


class Product(ClusterableModel, index.Indexed):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    seller_info = models.TextField()
    location = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('For Sale', 'For Sale'),
        ('Reserved', 'Reserved'),
        ('Sold', 'Sold'),
    )
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='For Sale'
    )

    search_fields = [
        index.AutocompleteField('title', partial_match=True),
        index.FilterField('category'),
    ]

    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('price'),
        FieldPanel('category'),
        FieldPanel('seller_info'),
        FieldPanel('location'),
        FieldPanel('status'),
        InlinePanel('images', label="Product Images"),
    ]
