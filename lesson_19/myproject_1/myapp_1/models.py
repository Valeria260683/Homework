from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
