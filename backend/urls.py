from django.contrib import admin
from django.urls import path, include

from shop.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # api schema
    path('', include('shop.urls', namespace='shop')),
    
    # api v1
    path('api/v1/', include(router.urls))
]
