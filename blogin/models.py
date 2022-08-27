from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name="Title", max_length=200)
    body = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.title

    class Meta:
        ordering  = ('-create_date',)

class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name="Post", related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.name
    
    class Meta:
        ordering  = ('-create_date',)
