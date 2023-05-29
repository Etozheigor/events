from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from events.models import (Organization, Event)
from .serializers import OrganizationCreateSerializer, EventCreateSerializer


class OrganizationCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Вьюсет для создания организаций."""

    queryset = Organization.objects.all()
    serializer_class = OrganizationCreateSerializer


class EventRetrieveListCreateViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Вьюсет для создания и получения мероприятий."""

    queryset = Event.objects.all()
    serializer_class = EventCreateSerializer
 