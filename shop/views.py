
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from . models import Contact, Customer, Category, Product, Order
from django.contrib.auth.hashers import check_password, make_password
  

# Create your views here.

def index(request):
    cart = request.session.get('cart')
    if not cart:
        request.session.cart = {}
    products = None
    category = Category.objects.all()
    category_id = request.GET.get('category')
    if request.method == 'GET':
        if category_id:
            products = Product.objects.filter(category=category_id)
        else:
            products = Product.objects.all()
        return render(request, 'shop/index.html', {'products': products, 'category': category})
    else:
        product = request.POST.get('product')
        print(product)
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print(' is', request.session['cart'])
        return redirect('index')


def cart(request): 
    if request.session.get('cart') == None:
        return HttpResponse("<h1>Add Items First</h1>") 
    else:
        ids = list(request.session.get('cart'))
        products = Product.objects.filter(id__in=ids)
    return render(request, 'shop/cart.html', {'products': products}) 
     


 

def checkout(request):
    if request.method == 'POST':

        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        ids = list(request.session.get('cart'))
        products = Product.objects.filter(id__in=ids)
        for product in products:
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id))
                          )
            if customer:              
                order.save()
                request.session['cart'] = {}
                return redirect('cart')
            else:
                return redirect('login')
            
       

def order(request):
    if request.method == 'GET':

        customer = request.session.get('customer')
        print(customer)
        orders = Order.objects.filter(customer=customer).order_by('-status')
        print(orders)
    return render(request, 'shop/order.html', {'orders': orders})


def signup(request):
    if request.method == 'GET':
        return render(request, 'shop/signup.html')

    else:

        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        customer = Customer(username=username, phone=phone,
                            password=password, email=email)
        error_msg = ""
        cust = Customer.objects.filter(email=email)
        if not username:
            error_msg = "User Name Required"
        if not phone:
            error_msg = "Phone Number Required"
        if not email:
            error_msg = "E-Mail Required"
        if not password:
            error_msg = "Password Required"
        if cust:
            error_msg = "E-Mail already Exist"
        if not error_msg:
            customer.password = make_password(customer.password)
            customer.save()
            print(customer)
            return redirect('login')
        else:
            return render(request, 'shop/signup.html', {'error': error_msg})


def login(request):
     
    if request.method == 'GET':
        
        return render(request, 'shop/login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        custo = request.session.get('email')
        error_msg = ""
        try:
            customer = Customer.objects.get(email=email)

            print(custo)
        except:
            return HttpResponse("Create Account First")
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                return redirect('index')
            else:
                error_msg = "Invalid Deatils"
        else:
            error_msg = "Invalid Details"
        return render(request, 'shop/login.html', {'error': error_msg})


def logout(request):
    if request.method == 'GET':
        request.session.clear()
        return redirect('login')


def contact(request):
    if request.method == 'GET':
        return render(request, 'shop/contact.html')
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(
            name=name, phone=phone, desc=desc, email=email
        )
        contact.save()
    return HttpResponse("Your message has been sent")


  