"""
URL configuration for caffinity project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from cafio.views import home,product,productdetails,addproduct,addproductform,delete,update,updateform,addcart,addcartform,cart,cdelete,buynow,orderform,purchased
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('product/',product),
    path('productdetails/<int:id>/',productdetails),
    path('addproduct/',addproduct),
    path('addproduct/addproductform/',addproductform),
    path('productdetails/<int:id>/delete/',delete),
    path('productdetails/<int:id>/update/',update),
    path('productdetails/<int:id>/update/updateform/',updateform),
    path('<int:id>/addcart/',addcart),
    path('<int:id>/addcart/addcartform/',addcartform),
    path('cart/',cart),  
    path('<int:id>/cdelete/',cdelete), 
    path('buynow/',buynow),
    path('orderconfirm/',orderform),

    # path('payment/<int:id>/',payment),
    path('purchased/<str:paymentid>/<str:orderid>/',purchased),

]
