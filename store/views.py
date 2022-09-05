from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

def home(request):
    products = Product.objects.all().filter(is_available=True)
    context = {'lstProducts':products}
    return render(request,'store/home.html', context)

def store(request, category_slug=None):
    categories = None
    products = None

    if(category_slug != None):
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        totalProducts = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        print(products)
        totalProducts = products.count()

    context = {'lstProducts':products,'totalProducts':totalProducts}
    return render(request,'store/store.html', context)

def productDetail(request, category_slug, product_slug):
    try:
        singleProduct = Product.objects.get(category__slug=category_slug, slug=product_slug.lower())
    except Exception as error:
        raise error
    
    context = {'singleProduct':singleProduct}
    return render(request, 'store/product_detail.html', context)
