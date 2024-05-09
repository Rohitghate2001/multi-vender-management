from django.urls import path ,include

from rest_framework import routers
from vender_management.views import venderAPIViews,POAPI

router=routers.SimpleRouter()

router.register(r'venders',venderAPIViews)
router.register(r'purchase_orders',POAPI)

urlpatterns = [
    
path('',include(router.urls))
]
