from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from app.models import slider , banner_area , Main_Category , Product , Category
from django.contrib import messages
from django.template.loader import render_to_string
from cart.cart import Cart

# Create your views here.

def BASE(request):

    return render(request, 'base.html')

def HOME(request):
    sliders = slider.objects.all()
    banners = banner_area.objects.all()
    main_category = Main_Category.objects.all().order_by('-id')
    products = Product.objects.filter(section__name='Top Deal For Day')

    context = {'sliders': sliders,
               'banners':banners,
               'main_category':main_category,
               'products':products}
    return render(request,'Main/home.html',context)


def PRODUCT_DETAIL(request,slug):
    product = Product.objects.filter(slug=slug)
    if product.exists():
        product = Product.objects.get(slug=slug)
    else:
        return redirect('404')
    context ={
        'product':product
    }
    return render(request,'product/product_detail.html',context)


def Error404(request):
    return render(request,'error/404.html')


def MY_ACCOUNT(request):
    return render(request,'accounts/my_account.html')

def REGISTER(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).first():
            messages.error(request, "This username is already taken")
            return redirect('my_account')

        if User.objects.filter(email=email).first():
            messages.error(request, 'Email is already exists')
            redirect('my_account')

        user = User(
            username=username,
            email = email,
            password = password,
                )
            # user.set_password(password)
        user.save()
        return redirect('my_account')
    return render(request,'accounts/my_account.html')

def LOGIN(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=authenticate(request,username=User.objects.get(email=username),password=password)
        except:
            user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Email and Password Are Invaild')
            return redirect('my_account')
    return render(request, 'accounts/my_account.html')


@login_required(login_url='/account/login')
def PROFILE(request):
    return render(request,'profile/profile.html')

@login_required(login_url='/accounts/login')
def PROFILE_UPDATE(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_id = request.user.id

        user = User.objects.get(id=user_id)
        user.username=username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name

        if password != None and password !="":
            user.set_password(password)
        user.save()
        messages.success(request,'Profile are successfully update !')
        return redirect('profile')
    return render('profile')

def BLOG(request):
    return render(request,'Main/blog.html')

def CONTACT(request):
    return render(request,'Main/contact.html')

def PRODUCT(request):
    category = Category.objects.all()
    product = Product.objects.all()
    context ={
        'category':category,
        'product':product
    }
    return render(request,'product/product.html',context)

def ABOUT(request):
    return render(request,'Main/about.html')


def filter_data(request):
    # categories = request.GET.getlist('category[]')
    # brands = request.GET.getlist('brand[]')
    #
    # allProducts = Product.objects.all().order_by('-id').distinct()
    # if len(categories) > 0:
    #     allProducts = allProducts.filter(Categories__id__in=categories).distinct()
    #
    # if len(brands) > 0:
    #     allProducts = allProducts.filter(Brand__id__in=brands).distinct()
    #
    #
    # t = render_to_string('ajax/product-list.html', {'product': allProducts})

    return JsonResponse({'data': "hello"})


@login_required(login_url="/account/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/account/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/account/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/account/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/account/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/account/login")
def cart_detail(request):
    return render(request, 'cart/cart.html')


