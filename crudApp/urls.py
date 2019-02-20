from django.contrib import admin
from django.urls import path, include

from products import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='home'),
    path('auth/', include('accounts.urls')),
]
