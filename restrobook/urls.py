from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', include('register.urls')),
    path('payment', include('register.urls')),
]
