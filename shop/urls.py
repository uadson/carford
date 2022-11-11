from django.urls import path

from rest_framework.routers import SimpleRouter
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from shop.views import (
    CarViewSet, CustomerViewSet, OrderViewSet, StoreViewSet
)

app_name = 'shop'

# Routes
router = SimpleRouter()
router.register('cars', CarViewSet)
router.register('customers', CustomerViewSet)
router.register('orders', OrderViewSet)
router.register('stores', StoreViewSet)

# Documentation
schema_view = get_schema_view(
    openapi.Info(
        title='CarFord Shop API',
        default_version='v1',
        description="A Car's Shop API from Nork-Town",
        terms_of_service="https://www.google.com/policies/terms/",
        license=openapi.License(name='MIT License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('carfordapi/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
