from django.db import models

class Blogs(models.Model):

    blog_category = models.CharField(max_length=200)
    blog_title = models.CharField(max_length=200)
    blog_content = models.CharField(max_length=30000)
    blog_summary = models.CharField(max_length=30000)



class Comments(models.Model):

    blog_id = models.IntegerField()
    comment_author = models.CharField(max_length=200)
    comment = models.CharField(max_length=1000, default="")
    comment_type = models.CharField(max_length=20)