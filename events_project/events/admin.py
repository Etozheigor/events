from django.contrib import admin

from .models import Organization, Event


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    """Кастомный класс для администрирования модели Organization."""

    search_fields = ('title', 'description', 'address', 'postcode')
    list_filter = ('title', 'description', 'address', 'postcode')
    list_display = ('title', 'description', 'address', 'postcode')


@admin.register(Event)
class IngredientAdmin(admin.ModelAdmin):
    """Кастомный класс для администрирования модели ингредиентов."""

    search_fields = ('title', 'description', 'date')
    list_filter = ('title', 'description', 'date')
    list_display = ('title', 'description', 'image_tag', 'date')
    ordering = ('date',)
