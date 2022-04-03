from django.contrib import admin

# Register your models here.
from webapp.models import Quote


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'author', 'email', 'rating', 'is_moderated', 'created_at']
    search_fields = ['text', 'author']
    fields = ['id', 'text', 'author', 'email', 'is_moderated', 'created_at']
    readonly_fields = ['id', 'created_at']


admin.site.register(Quote, QuoteAdmin)
