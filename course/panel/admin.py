from django.contrib import admin
from . import models

admin.site.register(models.UserProfile)
admin.site.register(models.Homework)
admin.site.register(models.Video)
admin.site.register(models.Upload)
