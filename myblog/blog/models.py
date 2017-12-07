from django.db import models


'''
数据模块
使用ORM模块
类似于MVC结构中的Models(模型
'''
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32,default='title')
    content = models.TextField(null=True)
    time = models.DateTimeField(auto_now=True)
    # 修改后台管理系统中数据默认显示名称
    def __str__(self):
        return self.title



