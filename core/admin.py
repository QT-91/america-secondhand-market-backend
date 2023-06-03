from wagtail.contrib.modeladmin.options import modeladmin_register
from product.admin import ProductAdmin


modelAdmins = (
    ProductAdmin,  
)

for idx, modelAdmin in enumerate(modelAdmins):
    modelAdmin.menu_order = (idx+1) * 10
    modeladmin_register(modelAdmin)
    print(f"Registered {modelAdmin.model.__name__} to admin")
