from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shop.models import Products

# Create your views here.
@api_view(['GET'])
def api_product(request):
    products = Products.objects.all()
    results = []
    for product in products:
        results.append({
            'title': product.title,
            'price' : product.price,
            'discount_price': product.discount_price,
            'category': product.category,
            'description':product.description,
            'image':product.image,
        })
    return Response(data=results,status=200)

@api_view(['GET'])
def api_view_products(request,products_id):
    try:
        products = Products.objects.get(id=products_id)
        result={
            'title': products.title,
            'price' :products.price,
            'discount_price': products.discount_price,
            'category':products.category,
            'description':products.description,
            'image':products.image,
        }
        return Response( data=result, status=200)
    except Products.DoesNotExist:
        return Response(data={'message': f"Report id{products_id} not found"},status=404)


@api_view(['POST'])
def api_add_products(request):
    created_id = Products.objects.create(**request.data)
    return Response(data={
        'message': f"Products id{created_id} not found"
    },status=201)

@api_view(['PUT'])
def api_update_products(request,products_id):
    try:
        products = Products.objects.get(id=products_id)
        products.title = request.data.get('title',products.title)
        products.price = request.data.get('price',products.price)
        products.discount_price = request.data.get('discount_price',products.discount_price)
        products.category = request.data.get('category', products.category)
        products.description = request.data.get('description', products.description)
        products.image = request.data.get('image', products.image)
        products.save()
        result={
            'title': products.title,
            'price' :products.price,
            'discount_price': products.discount_price,
            'category':products.category,
            'description':products.description,
            'image':products.image,
        }
        return Response(data={
        'message': f"Products update {products_id} successfull",
        'data': result
        },status=201)
    except Products.DoesNotExist:
        return Response(data={'message': f"Report id{products_id} not found"},status=404)

@api_view(['DELETE'])
def api_delete_products(request,products_id):
    try:
        products = Products.objects.get(id=products_id)
        products.delete()
        return Response(data={
            'message': f"Products delete{products_id} successfull",
        },status=204)
    except Products.DoesNotExist:
        return Response(data={'message': f"Report id{products_id} not found"},status=404)
