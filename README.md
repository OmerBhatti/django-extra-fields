# django-extra-fields

`django-extra-fields` is a Django package that allows you to attach and manage additional fields on any model dynamically. This package is designed to be simple and flexible, enabling you to add key-value pairs to any Django model without modifying the original model structure.

## Features

- Add custom key-value pairs to any Django model.
- Query and manage these fields easily.
- Supports Django's admin interface for easier management.

## Installation

You can install `django-extra-fields` via pip. Add it to your `requirements.txt` or install it directly using pip:

```bash
pip install django-extra-fields
```

## Usage
### Adding to Your Django Project
1. Add extra_fields to your INSTALLED_APPS:

    In your Django project's settings.py, add extra_fields to INSTALLED_APPS:
    
    ```python
    INSTALLED_APPS = [
        ...
        'extra_fields',
    ]
    ```

2. Extend Your Models:

    To add extra fields to a model, make your model inherit from ExtraFieldModel:
    
    ```python
    from django.db import models
    from extra_fields.models import ExtraFieldModel

    class MyModel(ExtraFieldModel):
        name = models.CharField(max_length=100)
    ```

3. Migrate Your Database:

    Create and apply migrations for the new extra_fields tables:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Use the Extra Fields:

    You can now use the set_extra_field, get_extra_field, and delete_extra_field methods to manage extra fields:

    ```python
    blog = Blog.objects.create(name="Example")
    blog.set_extra_field('color', 'blue')
    color = blog.get_extra_field('color')
    blog.delete_extra_field('color')
    ```

5. Add Inline editor on Admin panel

    Add ExtraFieldModelInline in inlines of the model Admin
    ```python
    from django.contrib import admin

    from .models import Blog
    from extra_field.admin import ExtraFieldModelInline

    class BlogAdmin(admin.ModelAdmin):
        """Admin for blog model."""

        list_display = ('title', 'content')
        inlines = [ExtraFieldModelInline]

    admin.site.register(Blog, BlogAdmin)
    ```
