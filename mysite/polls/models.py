import datetime 
from django.db import models
#导入时区模块
from django.utils import timezone 

class Question(models.Model):
    question_text = models.CharField(max_length=200)   #问题描述
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    #每个 Choice 对象都关联到一个 Question 对象 外键
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='author_headshots')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()

'''
改变数据库模型需要以下几步：
    编辑 models.py 文件，改变模型。
    运行 python manage.py makemigrations 为模型的改变生成迁移文件。
    运行 python manage.py migrate 来应用数据库迁移。
'''