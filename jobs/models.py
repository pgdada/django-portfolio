from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    description = MarkdownxField(blank=True)

    def __str__(self):
        return self.summary

    def formatted_description(self):
        return markdownify(self.description)
