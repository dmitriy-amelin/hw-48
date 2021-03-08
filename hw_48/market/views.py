from django.shortcuts import render, get_object_or_404, redirect
from market.forms import ProductForm
from market.models import Product, category_choices


def index_view(request):
    products = Product.objects.filter(balance__gt=0).order_by('category', 'name')

    return render(request, "index.html", {'products': products})


def product_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'product_view.html', context={'product': product})


def product_add(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'product_add.html', context={'form': form, 'choices': category_choices})