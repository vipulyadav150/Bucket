
from django.contrib import admin
from django.urls import path
from django.conf.urls import url , include
from .views import home_page,about_page,contact_page,register_page,login_page
urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', home_page),
    url('^about/$' ,view = about_page ,name = 'aboutpage'),
    url('^contact/$' ,view = contact_page ,name = 'contactpage'),
    url('^login/$' ,view = login_page ,name = 'loginpage'),
    url('^register/$' ,view = register_page ,name = 'registerpage'),

]
