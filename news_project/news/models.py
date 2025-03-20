from django.db import models

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    Author_name = models.CharField(max_length=255,null=True, blank=True)

    image = models.ImageField(upload_to="news_images/", blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True, related_name="news")

    def __str__(self):
        return self.title

