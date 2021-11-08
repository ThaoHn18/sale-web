"""ecomsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop import views
from shop import user
from myapi import views as views_api
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('<int:id>/',views.detail, name='detail'),
    path('checkout/',views.checkout,name='checkout'),
    path('register/',user.register_user,name='register'),
    path('login/',user.login_user,name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page="/"),name=("logout")),
    path('api-products/',views_api.api_product,name='api-products'),
    path('products/<int:products_id>/',views_api.api_view_products,name='products'),
    path('add-products/',views_api.api_add_products,name='add-products'),
    path('update-products/<int:products_id>/',views_api.api_update_products,name='update-products'),
    path('delete-products/<int:products_id>/',views_api.api_delete_products,name='delete-products'),
]
