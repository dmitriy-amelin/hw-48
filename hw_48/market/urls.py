from django.urls import path

from market.views import (
    index_view, product_view, product_add,

)

urlpatterns = [
    path('', index_view, name='product-list'),
    path('product/<int:pk>', product_view, name='product-view'),
    path('product/add', product_add, name='product-add'),

]