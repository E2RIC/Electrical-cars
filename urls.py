from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("furniture.urls")),
    path('furniture', include('django.contrib.auth.urls')),  
    path('homelogin/', LoginView.as_view(template_name='client.html'), name='homelogin'),
]