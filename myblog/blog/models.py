from django.db import models
from datetime import datetime
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Date, Nested, Boolean, \
analyzer, InnerObjectWrapper, Completion, Keyword,Text
#解决suggest使用analyzer报错问题
from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer
# 连接es服务
connections.create_connection(hosts=['localhost'])


'''
数据模块
使用ORM模块
类似于MVC结构中的Models(模型)
'''


# 解决suggest使用analyzer报错问题
class CustomAnalyzer(_CustomAnalyzer):
    def get_analysis_definition(self):
        return {}


ik_analyzer = CustomAnalyzer("ik_max_word", filter=["lowercase"])


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32, default='title')
    content = models.TextField(null=True)
    filename = models.CharField(max_length=50, default=None, null=True)
    time = models.DateTimeField(auto_now=True)  # 将auto_now改为null=True后可以在admin后台管理中修改文章发布时间

    # 修改后台管理系统中数据默认显示名称
    def __str__(self):
        return self.title


class ZhaoPinDoc(DocType):
    url = Keyword()
    company = Keyword()
    title = Text(analyzer="ik_smart")
    salary = Keyword()
    city = Keyword()
    working_years = Text(analyzer="ik_smart")
    degree = Text(analyzer="ik_smart")
    job_type = Text(analyzer="ik_smart")
    release_time = Text(analyzer="ik_smart")
    job_tags = Text(analyzer="ik_smart")
    job_advantage = Text(analyzer="ik_smart")
    job_desc = Text(analyzer="ik_smart")
    work_addr = Text(analyzer="ik_smart")
    suggest = Completion(analyzer=ik_analyzer)

    class Meta:
        index = "lagou"
        doc_type = "jobs"
