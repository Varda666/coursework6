from django.contrib import admin

from users.models import User, CustomGroup


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'password', 'phone', 'img')
    list_filter = ('email', 'password', 'phone', 'img')
    search_fields = ('email', 'password', 'phone', 'img')


@admin.register(CustomGroup)
class CustomGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name', 'permissions')
    search_fields = ('name', 'permissions')
