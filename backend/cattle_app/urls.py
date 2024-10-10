from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CattleViewSet, UserViewSet

router = DefaultRouter()
router.register(r'cattle', CattleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserViewSet.as_view({'get': 'list'}), name='users_list'),
]
