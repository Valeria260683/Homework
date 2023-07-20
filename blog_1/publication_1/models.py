from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    is_private = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.pk} - {self.title} - {self.is_private}"