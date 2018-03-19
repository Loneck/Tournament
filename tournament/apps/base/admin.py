from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
