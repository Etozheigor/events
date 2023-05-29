from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from events.models import Organization, Event
from .fields import Base64ImageField


class OrganizationCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для POST-запросов к модели Organization."""

    class Meta:
        model = Organization
        fields = ('title', 'description', 'address', 'postcode')


class EventCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для POST-запросов к модели Event."""

    image = Base64ImageField(required=True)
    organizations = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Organization.objects.all())
    
    class Meta:
        model = Event
        fields = ('title', 'description', 'organizations', 'image', 'date')

    def validate_organizations(self, value):
        if value:
            organization_list = []
            for organization in value:
                if organization in organization_list:
                    raise serializers.ValidationError(
                        'Организаторы мероприятия не должны повторяться!')
                organization_list.append(organization)
            return value
        raise serializers.ValidationError(
            'У мероприятия должен быть минимум один организатор!')