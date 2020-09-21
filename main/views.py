from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .filters import *
from django.forms import inlineformset_factory
from django.contrib.auth.forms import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import *
from .decorators import *
from django.contrib.auth.models import Group

# Create your views here.


@login_required(login_url='login')
@admin_only
@allowed_users(allowed_roles=['admin'])
def home(request):
    customer = Customer.objects.all()
    order = Order.objects.all()
    total_customer = customer.count()
    total_order = order.count()
    delivered = order.filter(status='Delivered').count()
    pending = order.filter(status='Delivery Pending').count()
    filterOrder = orderFilter(request.GET, queryset=order)
    order = filterOrder.qs
    context = {'customers': customer, 'orders': order,
               'total_customers': total_customer, 'total_order': total_order, 'delivered': delivered, 'pending': pending, 'filterOrder': filterOrder}

    return render(request, 'main/home.html', context)


@login_required(login_url='login')
@admin_only
def products(request):
    product = Product.objects.all()

    return render(request, 'main/products.html', {'products': product})


@login_required(login_url='login')
def customer(request, cid):
    customer = Customer.objects.get(id=cid)
    customer_name = customer.name
    customer_email = customer.email
    corders = customer.order_set.all()
    corders_count = customer.order_set.count()
    filterOrder = orderFilter(request.GET, queryset=corders)
    corders = filterOrder.qs
    context = {'customer': customer, 'corders': corders,
               'corders_count': corders_count, 'customer_name': customer_name, 'customer_email': customer_email, 'filterOrder': filterOrder}

    return render(request, 'main/dynamic/customer.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    context = {}
    return render(request, 'main/dynamic/user.html', context)


@login_required(login_url='login')
def createOrder(request):

    createOrder_form = OrderForm()
    if request.method == 'POST':
        createOrder_form = OrderForm(request.POST)
        if createOrder_form.is_valid():
            createOrder_form.save()
            return redirect('/')

    context = {'form': createOrder_form}

    return render(request, 'main/forms/order_form.html', context)


@login_required(login_url='login')
def createCustomerOrder(request, cid):
    OrderFormSet = inlineformset_factory(
        Customer, Order, fields=('product', 'status'), extra=5)
    customer = Customer.objects.get(id=cid)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'form': formset}
    return render(request, 'main/forms/order_form.html', context)


@login_required(login_url='login')
def updateOrder(request, oid):
    update = Order.objects.get(id=oid)
    updateOrder_form = OrderForm(instance=update)
    if request.method == 'POST':
        updateOrder_form = OrderForm(request.POST, instance=update)
        if updateOrder_form.is_valid():
            updateOrder_form.save()
            return redirect('/')

    context = {'form': updateOrder_form}

    return render(request, 'main/forms/order_form.html', context)


@login_required(login_url='login')
def deleteOrder(request, oid):

    ordered_product = Order.objects.get(id=oid)
    if request.method == 'POST':
        ordered_product.delete()
        return redirect('/')

    context = {'item': ordered_product, }
    return render(request, 'main/forms/delete.html', context)


@login_required(login_url='login')
def deleteCustomer(request, cid):

    customer = Customer.objects.get(id=cid)
    if request.method == 'POST':
        customer.delete()
        return redirect('/')

    context = {'item': customer, }
    return render(request, 'main/forms/delete.html', context)


@login_required(login_url='login')
def createCustomer(request):
    createCustomer_form = customerForm()
    if request.method == 'POST':
        createCustomer_form = customerForm(request.POST)
        if createCustomer_form.is_valid():
            createCustomer_form.save()
            return redirect('/')

    context = {'customerForm': createCustomer_form}

    return render(request, 'main/forms/customer_form.html', context)


@login_required(login_url='login')
def updateCustomer(request, cid):
    customer = Customer.objects.get(id=cid)
    updateForm = customerForm(instance=customer)
    if request.method == 'POST':
        updateForm = customerForm(request.POST, instance=customer)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('/')

    context = {'customerForm': updateForm}

    return render(request, 'main/forms/customer_form.html', context)


@login_required(login_url='login')
def createProduct(request):
    createProduct_form = productForm()
    if request.method == 'POST':
        createOrder_form = productForm(request.POST)
        if createOrder_form.is_valid():
            createOrder_form.save()
            return redirect('/')

    context = {'productForm': createProduct_form}

    return render(request, 'main/forms/product_form.html', context)


@login_required(login_url='login')
def updateProduct(request, pid):
    product = Product.objects.get(id=pid)
    updateForm = productForm(instance=product)
    if request.method == 'POST':
        updateForm = productForm(request.POST, instance=product)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('/products/')

    context = {'productForm': updateForm}

    return render(request, 'main/forms/product_form.html', context)


@unauthenticatedUser
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth = authenticate(request, username=username, password=password)
        if auth is not None:
            login(request, auth)
            return redirect('/')
        else:
            messages.info(request, 'Username or password is incorrect')
            return redirect('login')

    context = {}

    return render(request, 'main/forms/login.html', context)


@unauthenticatedUser
def registerPage(request):
    registerForm = createUserForm()
    if request.method == 'POST':
        registerForm = createUserForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save()
            username = registerForm.cleaned_data.get('username')
            setRegisterGroup = Group.objects.get(name='customer')
            user.groups.add(setRegisterGroup)
            messages.success(request, 'An account for ' +
                             username+' has been successfully registered.')
            return redirect('/login')

    context = {'registerForm': registerForm}

    return render(request, 'main/forms/register.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('/login')
