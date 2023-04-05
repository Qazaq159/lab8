from django.shortcuts import render
from django.http.response import JsonResponse
from api.models import Product, Category


# Create your views here.
def product_list(request, *args, **kwargs):
    products = Product.objects.all()
    return JsonResponse({'result': [product.to_json() for product in products]}, status=200)


def product(request, pk, **kwargs):
    try:
        product = Product.objects.get(id=pk)
    except:
        return JsonResponse({'result': 'Does not exist!'}, status=404)
    return JsonResponse({'result': product.to_json()}, status=200)


def category_list(request, *args, **kwargs):
    categories = Category.objects.all()
    return JsonResponse({'result': [category.to_json() for category in categories]}, status=200)


def category(request, pk, **kwargs):
    try:
        category = Category.objects.get(id=pk)
    except:
        return JsonResponse({'result': 'Does not exist!'}, status=404)
    return JsonResponse({'result': category.to_json()}, status=200)


def category_products(request, pk, **kwargs):
    try:
        category = Category.objects.get(id=pk)
    except:
        return JsonResponse({'result': 'Does not exist!'}, status=404)
    return JsonResponse({'result': [product.to_json() for product in category.product_set.all()]}, status=200)