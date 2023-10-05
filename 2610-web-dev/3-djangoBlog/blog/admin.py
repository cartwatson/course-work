from django.contrib import admin

from .models import blog
from .models import comment

# Register your models here.
admin.site.register(blog)
admin.site.register(comment)