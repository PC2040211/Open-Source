from django.contrib import admin
from django.urls import path
from account.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login_page,name="login"),
    path('register/',register_page,name="register")
]