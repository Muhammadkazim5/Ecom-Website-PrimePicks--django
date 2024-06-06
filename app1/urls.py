
from django.urls import path

from .views  import home,signup
from .views.login import Login,logout
from .views.cart import Cart
from .views.about import About,Services
from .views.checkout import Checkout
from .views.orderView import OrderView
from .middlewares.auth import authMiddleware
from .middlewares.redirectLogin import RedireactMiddleware
urlpatterns = [
    path('',home.index.as_view(),name='homepage'),
    path('signup/',signup.Signup.as_view(),name='signup'), 
    path('login/',Login.as_view(),name='login'), 
    path('logout/',logout,name='logout'),  
    path('about/',About.as_view(),name='about'),  
    path('services/',Services.as_view(),name='services'),  
    path('cart/',Cart.as_view(),name='cart'), 
    path('checkout/',RedireactMiddleware(Checkout.as_view()),name='checkout'), 
    path('orders/',authMiddleware(OrderView.as_view()) ,name='orders'), 
]