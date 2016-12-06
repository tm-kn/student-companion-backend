from django.contrib import admin

from .models import PlaceComment


@admin.register(PlaceComment)
class PlaceCommentAdmin(admin.ModelAdmin):
    pass
