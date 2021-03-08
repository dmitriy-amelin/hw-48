from django.shortcuts import render

from market.models import Product, category_choices

def index_view(request):
    products = Product.objects.filter(balance__gt=0)

    return render(request, "index.html", {'products': products})