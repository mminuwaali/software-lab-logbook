from . import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    list_filter = [*BaseUserAdmin.list_filter, "level"]
    list_display = [*BaseUserAdmin.list_display, "level", "group_names"]

    def group_names(self, model):
        return ", ".join(map(lambda x: x.name,model.groups.all())).title()
    
    fieldsets = (
        (None, {"fields": ("level","username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    
