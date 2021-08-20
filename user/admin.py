from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User
from .forms import UserAdminCreationForm, UserAdminUpdateForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

admin.site.unregister(Group)


class UserAdmin(BaseUserAdmin):
    form = UserAdminUpdateForm
    add_form = UserAdminCreationForm

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ("first_name", "last_name")}),
        ('Permissions', {'fields': ('staff', "superuser", "active")}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password_2')}
        ),
    )

    list_display = ["email", "staff", "superuser"]
    list_filter = ['staff']
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
