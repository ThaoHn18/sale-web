from django.core import paginator
from django.shortcuts import render
from .models import Order, Products
from django.contrib.auth.decorators import login_required #  bắt user đăng nhập mới activate chức năng
from django.core.paginator import Paginator # phân trang
# Create your views here.

def index(request):
    product_object = Products.objects.all()
    # Phần search
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_object =product_object.filter(title__icontains=item_name)
    # phân trang paginator code
    paginator = Paginator(product_object,4)
    page_number = request.GET.get('page')
    product_object = paginator.get_page(page_number)
    return render(
        request=request,
        template_name ='shop/index.html',
        context={
            'product_object':product_object
        }
    )


def detail(request,id):
    product_object = Products.objects.get(id=id)
    return render(
        request=request,
        template_name ='shop/detail.html',
        context={
            'product_object':product_object
        }
    )
@login_required(login_url='/login')
def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items','')
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total',"")
        order = Order(
            total=total,
            items=items,
            name=name,
            email=email,
            address=address,
            city=city,
            state=state,
            zipcode=zipcode,
        )  
        order.save()
    
    return render (request,'shop/checkout.html')





