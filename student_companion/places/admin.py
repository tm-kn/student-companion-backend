from django.contrib import admin

from .models import Place, PlaceCategory, PlaceTag


@admin.register(PlaceCategory)
class PlaceCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(PlaceTag)
class PlaceTagAdmin(admin.ModelAdmin):
    pass
