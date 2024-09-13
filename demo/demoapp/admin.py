from django.contrib import admin

from demoapp.models import Blog
from extra_field.admin import ExtraFieldModelInline


class BlogAdmin(admin.ModelAdmin):
    """Admin for blog model."""

    list_display = ('title', 'content')
    inlines = [ExtraFieldModelInline]


admin.site.register(Blog, BlogAdmin)
