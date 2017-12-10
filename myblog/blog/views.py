from django.shortcuts import render

from django.conf import settings
import os
# Create your views here.
'''
执行响应的代码所在模块
代码逻辑处理的主要地点
返回响应
项目中大部分代码均在这里编写
'''
'''
1.每个响应对应一个函数,函数必须返回一个响应
2.函数必须存在一个参数,一般约定为request
3.每个响应(函数)对应一个url

'''
from django.http import HttpResponse,HttpResponseRedirect
from . import models

def index(request):
    # return HttpResponse('hello world')
    # article = models.Article.objects.get(pk=1)
    # articles = models.Article.objects.all()
    return render(request,'blog/index.html')

def blog(request):
    articles = models.Article.objects.all()  # all获取所有文章集合
    return render(request,'blog/blog.html',{'articles':articles})


def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})


def edit_page(request,article_id):
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')  #如果文章不存在,就新建文章
    else:
        # 如果文章存在,取得文章对象,传给edit_page
        article = models.Article.objects.get(pk=article_id)
        return render(request,'blog/edit_page.html',{'article':article})

import PIL.Image
def save_files(file):
    # with open(settings.BASE_DIR + os.sep + r'blog\static\%s' % file.name, 'wb') as f:
    #     for chunk in file.chunks():
    #         f.write(chunk)
    image = PIL.Image.open(file)
    image.save(settings.BASE_DIR + os.sep + r'blog\static\%s' % file.name,'jpeg')  # 此方法保存的图片不是原来的大小

def edit_action(request):
    title = request.POST.get('title','TITLE')  # 获取post过来的表单数据
    content = request.POST.get('content','CONTENT')
    file = request.FILES.get('file',None)
    article_id = request.POST.get('article_id','0')  #article_id默认为0
    if str(article_id) == '0' and file:  # 如果新建文章,上传了文件
        save_files(file)
        models.Article.objects.create(title = title,content = content,filename = file.name)  # 连接数据库增加文章
        articles = models.Article.objects.all()
        return render(request,'blog/blog.html',{'articles':articles}) # 提交完成后返回博客列表页面
    elif str(article_id) == '0' and  not file:  # 如果新建文章,无上传文件
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'blog/blog.html', {'articles': articles})  # 提交完成后返回博客列表页面
    elif str(article_id) != '0' and  not file:  # 如果是修改文章,并且没有上传文件,则保持原文件不变,获取新的title和content
        article = models.Article.objects.get(pk=article_id)
        article.title = title
        article.content = content
        article.filename = article.filename
        article.save()
        return render(request, 'blog/article_page.html', {'article': article})
    else:  # 如果修改文章,且上传了文件,则获取article对象的新内容保存
        article = models.Article.objects.get(pk=article_id)
        article.title = title
        article.content = content
        article.filename = file
        article.filename = file.name
        save_files(file)
        article.save()
        return render(request, 'blog/article_page.html', {'article': article})


def delete_article(request,article_id):
    models.Article.objects.filter(pk=article_id).delete()  # 删除数据库中对应id的文章
    articles = models.Article.objects.all()  # all获取所有文章集合
    return render(request, 'blog/blog.html', {'articles': articles})


'''TODO 
1.自己可以编辑文章,别人只能看?
2.页面编辑器
3.文件上传(已经实现,没有独立出来),下载
4.添加天气显示
5.添加娱乐模块,集成豆瓣电影?音乐?书?
6.搞笑段子?
7.搜索引擎功能?
...
'''