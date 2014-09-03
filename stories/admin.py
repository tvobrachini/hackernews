#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: tiago.brachini
# @Date:   2014-09-02 14:21:53
# @Last Modified by:   tiago.brachini
# @Last Modified time: 2014-09-02 15:41:33
from django.contrib import admin
from .models import Story


class StoryAdmin(admin.ModelAdmin):

    list_display = (
        "__unicode__",
        "domain",
        "moderator",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "title",
        "moderator__username",
        "moderator__first_name",
        "moderator__last_name",
    )

    list_filter = ("created_at", "updated_at", )

    fieldsets = [
        ("Story", {
            "fields": ("title", "url", "points", )
            }
         ),
        ("moderator", {
            "classes": ("collapse", ),
            "fields": ("moderator", )
            }
         ),
        ("Change History", {
            "classes": ("collapse", ),
            "fields": ("created_at", "updated_at", )
            }
         )
    ]

    readonly_fields = ("created_at", "updated_at")

admin.site.register(Story, StoryAdmin)
