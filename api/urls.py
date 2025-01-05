from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TagViewSet, PropertyViewSet, CommentsViewSet, UserViewSet

router = DefaultRouter()
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'properties', PropertyViewSet, basename='property')
router.register(r'comments', CommentsViewSet, basename='comments')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
