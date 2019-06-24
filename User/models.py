from django.db import models

# Create your models here.

class Tddsquestions(models.Model):
    """问题表"""
    question_id = models.BigIntegerField()             #问题ID
    question_desc = models.CharField(max_length=255,blank=False)    #问题内容
    question_tags = models.CharField(max_length=255,blank=True)     #问题标签
    question_next = models.CharField(max_length=255,blank=True)     #不知道
    created_time = models.DateTimeField()                           #创建时间


class Tddsanswers(models.Model):
    """答案表"""
    answer_id = models.BigIntegerField()               #答案ID
    question_id = models.BigIntegerField()             #所属问题ID
    answer_desc = models.CharField(max_length=255,blank=False)      #答案内容
    created_time = models.DateTimeField()                           # 创建时间


"""
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)  # 文章摘要，可为空
    category = models.ForeignKey(Category, on_delete=True)  # ForeignKey表示1对多（多个post对应1个category）
    tags = models.ManyToManyField(Tag, blank=True)
    views = models.PositiveIntegerField(default=0)  # 阅读量
"""


