from statistics import mode
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

# BLOG
class blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    posted = models.DateTimeField('date published')
    def __str__(self):
        return self.content
    def get_comments(self):
        commentList = []
        comments = comment.objects.order_by('-posted')
        for i in comments:
            if i.blog.id == self.id:
                commentList.append(i)
        return commentList
    def get_comment_count(self):
        return str(len(self.get_comments()))

# COMMENT
class comment(models.Model):
    blog = models.ForeignKey('blog', on_delete=models.CASCADE)
    commenter = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    posted = models.DateTimeField('date published')
    def __str__(self):
        return self.content
