from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import OrganizationCreateViewSet, EventRetrieveListCreateViewSet

app_name = 'api'

v1_router = DefaultRouter()

v1_router.register('organizations', OrganizationCreateViewSet, basename='organization')
v1_router.register('events', EventRetrieveListCreateViewSet, basename='event')


urlpatterns = [
    path('', include(v1_router.urls)),
    # path('', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
]