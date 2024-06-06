from django.shortcuts import render,redirect
from django.views import View
from app1.models.orders import Order
# from app1.middlewares.auth import authMiddleware
# from django.utils.decorators import method_decorator
class OrderView(View):
    # @method_decorator(authMiddleware)
    def get(self,request):
        customer=request.session.get('customer')
        orders=Order.get_orders_by_customer(customer)
       
        return render(request,'order.html',{'orders':orders})