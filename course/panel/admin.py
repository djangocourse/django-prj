from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

class UserProfileAdmin(UserAdmin):
    list_display = ('username', 'is_teacher')
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('username', 'password', 'is_teacher', 'code')}),)

    ordering = ('username',)
    filter_horizontal = ()

admin.site.register(models.UserProfile, UserProfileAdmin)
admin.site.register(models.Homework)
admin.site.register(models.Video)
admin.site.register(models.Upload)
