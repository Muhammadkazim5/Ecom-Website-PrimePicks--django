from django.shortcuts import render,redirect
from django.views import View
class About(View):
    def get(self,request):
        return render(request,'about.html')
class Services(View):
    def get(self,request):
        return render(request,'services.html')
