from . import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    list_display = [*BaseUserAdmin.list_display, "group_names"]

    def group_names(self, model):
        return ", ".join(map(lambda x: x.name,model.groups.all())).title()
