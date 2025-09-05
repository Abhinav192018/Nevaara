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
    path('clearance/', views.Clearance_sale, name='clearance_sale'),
    path('gallery/', views.Gallery, name='gallery'),
    path('contact/', views.Contact, name='contact'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
