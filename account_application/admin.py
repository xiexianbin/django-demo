# -*- coding: utf-8 -*-

from django.contrib import admin
from account_application.models import User


class UserControl(admin.ModelAdmin):
    list_display = ('nickname',)
    search_fields = ('nickname',)
    ordering = ('-id',)


admin.site.register(User, UserControl)
