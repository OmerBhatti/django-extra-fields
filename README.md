# django-extra-model-fields

`django-extra-model-fields` is a Django package that allows you to attach and manage additional fields on any model dynamically. This package is designed to be simple and flexible, enabling you to add key-value pairs to any Django model without modifying the original model structure.

## Features

- Add custom key-value pairs to any Django model.
- Query and manage these fields easily.
- Supports Django's admin interface for easier management.

## Installation

You can install `django-extra-model-fields` via pip. Add it to your `requirements.txt` or install it directly using pip:

```bash
pip install django-extra-model-fields
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
    blog = Blog.objects.create(title="Intorduction to Computers", content="<p>blog body goes here</p>")

    # setting key value
    blog.set_value('author', 'John Smith')
    blog.set_value('meta_data', {'clicks': 100, 'views': 200})

    # getting values
    blog.get_value('author')  # returns a string: 'John Smith'
    blog.get_value('meta_data')  # returns a python dict: {'clicks': 100, 'views': 200}

    # getting all keys
    blog.get_keys()  # return a queryset ['author', 'meta_data']

    # deleting a key-value pair
    blog.delete_key('author')
    ```

5. Filtering

    ```python
    # list all extra_fields
    blog.extra_fields.all()  # returns a query set of <ExtraField>

    # filter on extra_fields
    Blog.objects.filter(extra_fields__key='author', extra_fields__value='John Smith')
    Blog.objects.filter(extra_fields__value__clicks__gte=100)
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
