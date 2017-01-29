from django.contrib import admin

from .models import Place, PlaceCategory, PlaceImage, PlaceTag


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 0
    readonly_fields = ('image_height', 'image_width')


@admin.register(PlaceCategory)
class PlaceCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = (PlaceImageInline,)


@admin.register(PlaceTag)
class PlaceTagAdmin(admin.ModelAdmin):
    pass
