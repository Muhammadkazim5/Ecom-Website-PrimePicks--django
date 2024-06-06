from django.shortcuts import render,redirect
from django.views import View
from app1.models.orders import Order
from app1.models.product import Product
from app1.models.customer import Customer
class Checkout(View):
    def post(self,request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer=request.session.get('customer')
        cart=request.session.get('cart')
        products=Product.get_product_by_id(list(cart.keys())) 
        for product in products:
            order=Order(customer=Customer(id=customer),product=product,price=product.price,address=address,phone=phone,quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart']={}
        return redirect('orders')


