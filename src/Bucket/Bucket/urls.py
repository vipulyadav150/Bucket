
from django.contrib import admin
from django.urls import path
from django.conf.urls import url , include
from django.conf import settings
from django.conf.urls.static import static
from .views import home_page,about_page,contact_page,register_page,login_page
from Products.views import ProductListView,product_list_view,ProductDetailView,product_detail_view


urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', home_page),
    url('^about/$' ,view = about_page ,name = 'aboutpage'),
    url('^contact/$' ,view = contact_page ,name = 'contactpage'),
    url('^login/$' ,view = login_page ,name = 'loginpage'),
    url('^register/$' ,view = register_page ,name = 'registerpage'),
    url('^products/$' ,view = ProductListView.as_view()),
    url('^products-fbv/$' ,view = product_list_view),
    url('^products/(?P<pk>\d+)/$' ,view = ProductDetailView.as_view()),
    url('^products-fbv/(?P<pk>\d+)/$' ,view = product_detail_view),


]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
