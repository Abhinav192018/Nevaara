from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('products/', views.Products, name='products'),
    path('product/details/', views.Product_Detail, name='product_detail'),
    # path('clearance/', views.Clearance_sale, name='clearance_sale'),
    path('gallery/', views.Gallery, name='gallery'),
    path('contact/', views.Contact, name='contact'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path("cart/",views.Cart,name='cart'),
    path('myaccount/',views.Myaccount,name='myaccount'),
    path('orders/',views.Orders,name='orders'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
