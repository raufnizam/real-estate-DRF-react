from django.contrib import admin
from .models import Property, Tag, Comments

# Register your models here.

admin.site.register(Comments)
admin.site.register(Tag)
admin.site.register(Property)
