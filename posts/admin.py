# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdminModel(admin.ModelAdmin):
    list_display = ["title","updated","timestamp"]
    list_display_links = ["updated"]
    search_fields = ["title","content"]
    list_filter = ["updated","timestamp"]
    list_editable = ["title"]



    class Meta:
        model = Post

admin.site.register(Post,PostAdminModel)
