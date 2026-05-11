from django.contrib import admin

from django.contrib.auth.models import User

from .models import FileUpload


# FILE UPLOAD ADMIN

class FileUploadAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'file')

    search_fields = ('user__username', 'file')

    list_filter = ('user',)


# REGISTER MODELS

admin.site.register(FileUpload, FileUploadAdmin)
