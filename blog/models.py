from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE,)
    body = models.TextField()
    slug = models.SlugField(null=True)
    
    def __str__(self):
        return self.title
    
    #associates each resource from blog detail with an absolute url
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})