# things/admin.py

from django.contrib import admin
from .models import Thing


@admin.register(Thing)
class ThingAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name", "description")
    list_filter = ("created_at",)
