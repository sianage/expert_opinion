from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #id = pk
        return reverse('econ_blog', args=(str(self.id)))
        #return reverse('econ_blog')

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = models.TextField()
    body = RichTextField(blank=True, null=True)
    category = models.CharField(max_length=255, default='no category')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #id = pk
        return reverse('econ_blog', args=(str(self.id)))
        #return reverse('econ_blog')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.post.title, self.author)

