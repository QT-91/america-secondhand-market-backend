from wagtail.contrib.modeladmin.options import ModelAdmin
from .models import Product


class ProductAdmin(ModelAdmin):
    model = Product
    menu_label = 'Products'
    menu_icon = 'folder-open-inverse'
    menu_order = 200
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('title', 'price', 'category', 'status')
    list_filter = ('category', 'status')
    search_fields = ('title',)
