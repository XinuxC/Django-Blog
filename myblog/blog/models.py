from django.db import models
from datetime import datetime
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Date, Nested, Boolean, \
analyzer, InnerObjectWrapper, Completion, Keyword,Text
#解决suggest使用analyzer报错问题
from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer

'''
数据模块
使用ORM模块
类似于MVC结构中的Models(模型)
'''


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32,default='title')
    content = models.TextField(null=True)
    filename = models.CharField(max_length=50,default=None,null=True)
    time = models.DateTimeField(auto_now=True)  # 将auto_now改为null=True后可以在admin后台管理中修改文章发布时间
    # 修改后台管理系统中数据默认显示名称
    def __str__(self):
        return self.title

#连接es服务
connections.create_connection(hosts=['localhost'])


class CustomAnalyzer(_CustomAnalyzer):
    def get_analysis_definition(self):
        return {}


ik_analyzer = CustomAnalyzer("ik_max_word",filter=["lowercase"])


class ZhaopinDoc(DocType):
    company = Text(analyzer="ik_smart")
    title = Text(analyzer="ik_max_word")
    salary = Text()
    job_tags = Text()
    job_desc = Text()
    suggest = Completion(analyzer=ik_analyzer)

    class Meta:
        index = 'zhaopin'
        doc_type = 'Jobs'



