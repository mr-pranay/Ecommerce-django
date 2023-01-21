from django.contrib import admin
from backend.models import ProductModel,CustomerModel,CartModel,OrdersModel

class DetailsAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProductModel,DetailsAdmin)
admin.site.register(CustomerModel,DetailsAdmin)
admin.site.register(CartModel,DetailsAdmin)
admin.site.register(OrdersModel,DetailsAdmin)