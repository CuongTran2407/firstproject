from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import  views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),

    #home, blog , contact
    path('',views.HOME,name='home'),
    path('product/<slug:slug>',views.PRODUCT_DETAIL,name='product_detail'),
    path('product/',views.PRODUCT,name='product'),
    path('blog/',views.BLOG,name='blog'),
    path('contact/',views.CONTACT,name='contact'),
    path('about/',views.ABOUT,name='about'),
    path('product/filter-data', views.filter_data, name="filter-data"),

    #error
    path('404',views.Error404,name='404'),

    #account
    path('account/my-account',views.MY_ACCOUNT,name='my_account'),
    path('account/register',views.REGISTER,name='register'),
    path('account/login',views.LOGIN,name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    #profile
    path('profile/',views.PROFILE,name='profile'),
    path('profile/update', views.PROFILE_UPDATE, name='profile_update'),

    #cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),
    # path('product/<slug:slug>',views.cart_slug,name='cart_slug'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
