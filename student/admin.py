from . import models
from django.contrib import admin


@admin.register(models.Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "created_at", "updated_at"]
    list_filter = ["user"]
    search_fields = ["title"]


@admin.register(models.Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_filter = ["user"]
    search_fields = ["description"]
    list_display = ["description", "user", "created_at", "updated_at"]
