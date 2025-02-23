from django.contrib import admin
from .models import ContentItem

@admin.register(ContentItem)
class ContentItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'date', 'order')
    list_filter = ('section',)
    search_fields = ('title', 'text')
    ordering = ('order', 'date')