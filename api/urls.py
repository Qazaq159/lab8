from django.urls import path
from api.views import product_list, product, category_list, category, category_products


urlpatterns = [
    path('products/', product_list),
    path('products/<int:pk>', product),
    path('categories/', category_list),
    path('categories/<int:pk>', category),
    path('categories/<int:pk>/products', category_products)
]