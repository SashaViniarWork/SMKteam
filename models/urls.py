from django.urls import path, include
from .views import GroundViewSet, EventViewSet, ResponseViewSet
from rest_framework import routers

router1 = routers.DefaultRouter()
router1.register('grounds', GroundViewSet)

router2 = routers.DefaultRouter()
router2.register('events', EventViewSet)

router3 = routers.DefaultRouter()
router3.register('responses', ResponseViewSet)

urlpatterns = [
    path('', include(router1.urls)),
    path('', include(router2.urls)),
    path('', include(router3.urls)),
]
