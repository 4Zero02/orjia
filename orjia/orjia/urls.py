from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('atletica/', include('atletica.urls')),
    path('modalidade/', include('modalidade.urls')),
]
