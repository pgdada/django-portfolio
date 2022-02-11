from django.contrib import admin
from .models import Job
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.
admin.site.register(Job, MarkdownxModelAdmin)
