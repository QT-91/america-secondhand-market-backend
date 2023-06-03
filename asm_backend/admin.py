from wagtail.contrib.modeladmin.options import modeladmin_register
from product.admin import ProductAdmin


modelAdmins = (
    ProductAdmin,  
)

for idx, modelAdmin in enumerate(modelAdmins):
    modelAdmin.menu_order = (idx+1) * 100
    modeladmin_register(modelAdmin)
