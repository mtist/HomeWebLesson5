from django.contrib import admin
from django.urls import path, include
from pages.views import home, pages
from django.conf import settings
from django.conf.urls.static import static
import products.urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', home, name='home'),
    path('<slug:slug>', pages, name='pages'),

    path('products/', include(products.urls, namespace='products',)),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)