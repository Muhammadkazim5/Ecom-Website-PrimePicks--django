from django.shortcuts import render,redirect
from django.views import View
from app1.models.product import Product
class Cart(View):
    def get(self,request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_product_by_id(ids)
        return render(request,'cart.html',{'products':products})



       