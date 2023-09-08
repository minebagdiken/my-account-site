from django.contrib import admin
from .models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active", "is_home", "slug", "selected_categories")
    list_editable = ("is_active", "is_home",)   # tikleri aktif etme kaldırma
    search_fields = ("title", "description",)
    list_filter =("is_active",)

    def selected_categories(self, obj):
        html= obj.category
        return html

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)

