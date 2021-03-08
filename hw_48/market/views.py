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
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = Product.objects.create(
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description'),
                category=form.cleaned_data.get('category'),
                balance=form.cleaned_data.get('balance'),
                price=form.cleaned_data.get('price')
            )
            return redirect('product-view', pk=product.id)
        return render(request, 'product_add.html', context={'form': form, 'choices': category_choices})


def product_update(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == 'GET':
        form = ProductForm(initial={
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'balance': product.balance,
            'price': product.price
        })
        return render(request, 'product_update.html', context={'form': form, 'product': product})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = request.POST.get("name")
            product.description = request.POST.get("description")
            product.category = request.POST.get("category")
            product.balance = request.POST.get("balance")
            product.price = request.POST.get("price")
            product.save()
            return redirect('product-view', pk=product.id)

        return render(request, 'product_update.html', context={'form': form, 'product': product})