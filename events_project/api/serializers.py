from djoser.serializers import \
    UserCreateSerializer as DjoserUserCreateSerializer
from rest_framework import serializers

from events.models import Event, Organization
from users.models import User

from .fields import Base64ImageField


class UserCreateSerializer(DjoserUserCreateSerializer):
    """Сериализатор для POST-запросов к модели User."""

    class Meta:
        model = User
        fields = (
            'email', 'username', 'password', 'organization')


class UserReadSerializer(serializers.ModelSerializer):
    """Сериализатор для получения отображения пользователей в организациях."""

    class Meta:
        model = User
        fields = ('email', 'username')


class OrganizationCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для POST-запросов к модели Organization."""

    class Meta:
        model = Organization
        fields = ('title', 'description', 'address', 'postcode')


class OrganizationReadSerializer(serializers.ModelSerializer):
    """Сериализатор для получения организации со всеми ее участниками."""

    address_postcode = serializers.SerializerMethodField()
    users = UserReadSerializer(many=True)

    class Meta:
        model = Organization
        fields = ('title', 'description', 'address_postcode', 'users')

    def get_address_postcode(self, obj):
        return f'{obj.address}, {obj.postcode}'


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

    def create(self, validated_data):
        organizations = validated_data.pop('organizations')
        event = Event.objects.create(**validated_data)
        for organization in organizations:
            event.organizations.add(organization)
        return event


class EventReadSerializer(serializers.ModelSerializer):
    """Сериализатор для GET-запросов к модели Event."""

    organizations = OrganizationReadSerializer(many=True)

    class Meta:
        model = Event
        fields = ('title', 'description', 'image', 'date', 'organizations')
