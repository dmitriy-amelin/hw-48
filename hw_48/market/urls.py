from django.urls import path

from market.views import (
    index_view,

)

urlpatterns = [
    path('', index_view, name='product-list'),

]