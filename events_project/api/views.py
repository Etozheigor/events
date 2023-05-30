from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination

from events.models import Event, Organization

from .serializers import (EventCreateSerializer, EventReadSerializer,
                          OrganizationCreateSerializer)


class OrganizationCreateViewSet(
    mixins.CreateModelMixin, viewsets.GenericViewSet
):
    """Вьюсет для создания организаций."""

    queryset = Organization.objects.all()
    serializer_class = OrganizationCreateSerializer


class EventRetrieveListCreateViewSet(
    mixins.RetrieveModelMixin, mixins.CreateModelMixin,
    mixins.ListModelMixin, viewsets.GenericViewSet
):
    """Вьюсет для создания и получения мероприятий."""

    queryset = Event.objects.all()
    serializer_class = EventCreateSerializer
    filter_backends = (
        DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('date',)
    search_fields = ('^title',)
    ordering_fields = ('date',)
    pagination_class = LimitOffsetPagination

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return EventReadSerializer
        return EventCreateSerializer
