from django.contrib import admin


'''当前应用的后台管理系统配置'''
# Register your models here.
from . import models

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','time')  #后台管理文章显示需要的字段,list和tuple都可以(用tuple是因为不可变,安全)字段名需和models里的一致
    list_filter = ('time',)  # 后台admin管理页面中显示时间过滤器


admin.site.register(models.Article,ArticleAdmin)