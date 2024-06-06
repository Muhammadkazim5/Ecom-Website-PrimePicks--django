from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from app1.models.customer import Customer
from django.views import View
class Signup(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        postData=request.POST
        first_name=postData.get('firstname')
        last_name=postData.get('lastname')
        phone=postData.get('phone')
        email=postData.get('email')
        password=postData.get('password')
        #value
        value={
            'first_name':first_name,
            'last_name':last_name,
            'email':email,
            'phone':phone,
            
        }
        customer=Customer(first_name=first_name,last_name=last_name,phone=phone,email=email,  password=password)
        #validation
        error_message=None
        if(not first_name):
            error_message="First Name Required!!"
        elif len(first_name)<3:         
            error_message="First Name must be 3 char long or more"
        elif not last_name:         
            error_message="Last Name Required!!"
        elif len(last_name)<3:         
            error_message="Last Name must be 3 char long or more"
        elif not phone:         
            error_message="Phone Number Required!!"
        elif len(phone)<11:         
            error_message="Phone Number must be 11 char long"
        elif not email:         
            error_message="Email Required!!"
        elif len(email)<5:         
            error_message="Email must be 5 char long"
        elif not password:         
            error_message="Password Required!!"
        elif len(password)<6:         
            error_message="Password  must be 6 char long"
        elif customer.isExists():       
            error_message="Email Already Exists"
        #save
        if not error_message:
            customer.password=make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data={
                'error':error_message,
                'value':value
            }
            return render(request,'signup.html',data)  
