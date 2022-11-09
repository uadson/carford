from rest_framework.routers import SimpleRouter

from shop.views import (
    CarViewSet, CustomerViewSet, OrderViewSet, StoreViewSet
)

app_name = 'shop'

router = SimpleRouter()
router.register('cars', CarViewSet)
router.register('customers', CustomerViewSet)
router.register('orders', OrderViewSet)
router.register('stores', StoreViewSet)
