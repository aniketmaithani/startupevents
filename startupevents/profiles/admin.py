# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = (
        'user',
        'mobile',
        'work_location')
    search_fields = ('user__username', 'mobile')
    list_filter = ('user',)


admin.site.register(UserProfile, UserProfileAdmin)
