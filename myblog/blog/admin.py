from django.contrib import admin


'''当前应用的后台管理系统配置'''
# Register your models here.

from . import models
admin.site.register(models.Article)