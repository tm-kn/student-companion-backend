from django.contrib import admin

from .models import PlaceRating


@admin.register(PlaceRating)
class PlaceRatingAdmin(admin.ModelAdmin):
    pass
