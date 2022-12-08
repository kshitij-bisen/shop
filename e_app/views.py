from django.shortcuts import render
from django.views import View
from .models import Customer,Product,Cart,OrderPlaced
from .form import CustomerRegistrationForm
from django.contrib import messages
# Create your views here.

# def index(r):
#     return render(r,'e_app/home.html')

class HomeView(View):
    def get(self,r):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')

        context = {'bottomwears':bottomwears,
                   'topwears':topwears}
        return render(r,'e_app/home.html',context)


# def product_detail(r):
#     return render(r ,'e_app/productdetails.html')

class ProductDetailView(View):
    def get(self,r,pk):
        product = Product.objects.get(pk=pk)
        return render(r ,'e_app/productdetails.html',{'data':product})


# def mobile(r):
#     return render(r ,'e_app/mobile.html')

def mobile(r,data=None):
    if data==None:
        mobiles = Product.objects.filter(category='M')
    elif data == 'redmi' or data == 'samsung':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == "below":
        mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=20000)
    elif data == "above":
        mobiles = Product.objects.filter(category='M').filter(discounted_price__gt=20000)

    return render(r ,'e_app/mobile.html',{'mobiles': mobiles})

def add_to_cart(r):
    return render(r ,'e_app/addtocart.html')

def buy_now(r):
    return render(r ,'e_app/buynow.html')

def orders(r):
    return render(r,'e_app/orders.html')

def checkout(r):
    return render(r,'e_app/checkout.html')

def profile(request):
 return render(request, 'e_app/profile.html')

def address(request):
 return render(request, 'e_app/address.html')


def change_password(request):
 return render(request, 'e_app/changepassword.html')

def login(request):
 return render(request, 'e_app/login.html')

# def customerregistration(request):
#     form = CustomerRegistrationForm()
#     if request.method == 'POST':
#         form = CustomerRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request,'e_app/customerregistration.html')
#     return render(request, 'e_app/customerregistration.html',{'form':form})

class customerregistration(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, 'e_app/customerregistration.html', {'form': form})
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations !! Registered sucessfully')
            form.save()
        return render(request,'e_app/customerregistration.html',{'form': form})