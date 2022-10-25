# from django.contrib import admin
from django.urls import path,include
from .views import Url
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include('app.urls'))
    path('',Url.as_view(),name="url"),
   

]
