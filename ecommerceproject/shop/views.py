from django.contrib import messages, auth

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger


# Create your views here.



def allprodCat(request,c_slug=None):
    c_page=None
    products_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products_list=Product.objects.all().filter(category=c_page,available=True)
    else:
        products_list=Product.objects.all().filter(available=True)

    paginator=Paginator(products_list,12)
    page=request.GET.get('page')
    try:
        products_list=paginator.page(page)
    except PageNotAnInteger:
        products_list=paginator.page(1)
    except EmptyPage:
        products_list=paginator.page(paginator.num_pages)


    return render(request,'category.html',{'category':c_page,'products':products_list,'page':page})

def proDetail(request,c_slug,product_slug):
    try:

        product=Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')




def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        myuser=User.objects.create_user(username=username,password=password)
        myuser.save()
        messages.success(request, 'submitted successfully.')
        return render(request, 'login.html')

    return render(request,'signup.html')

def login_view(request):
    if request.method=='POST':
        username=request.POST['use']
        password=request.POST['pas']
        user=auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request, 'your order has placed')
            return render(request,'checkout.html')
        else:
            messages.success(request,'username and password note valid')

            return render(request,'login.html')

    else:
        return render(request,'login.html')

def sort(request):
    return render(request,'sort.html')


def lwtohi(request):
    data=Product.objects.all().order_by('price')
    return render(request,'sort.html',{'data':data})

def hitolw(request):
    data=Product.objects.all().order_by('-price')
    return render(request,'sort.html',{'data':data})
