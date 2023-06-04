"""
URL configuration for project_practise_repo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from app_accounts import views as acc_view
from app_home import views as hom
from app_cart import views as cart
from app_customers import views as customer
from app_inventory import views as inventory


urlpatterns = [
    # admin route
    path('admin/', admin.site.urls),

    # accounts route
    path('playground/', include('playground.urls')),
    path('accounts/login',acc_view.login, name="login"),
    path('accounts/profile',acc_view.profile, name="profile"),
    path('accounts/register',acc_view.register, name="register"),

    # cart route
    path('cart/cart',cart.cart,name="cart"),

    # home route
    path('home/home',hom.home,name="Home"),

    # customers route
    path("customer/create",customer.create,name="Create"),
    path("customer/edit",customer.edit,name="Edit"),
    path("customer/index",customer.index,name="Index"),
    path("customer/show",customer.show,name="Show"),

    # inventory routes
    path('inventory/add',inventory.inv_add,name="Inventory-add"),
    path('inventory/edit',inventory.inv_edit,name="Inventory-edit"),
    path('inventory/list',inventory.inv_list,name="Inventory-list"),
    path('inventory/show',inventory.inv_show,name="Inventory-show"),
]