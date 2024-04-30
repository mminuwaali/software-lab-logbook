from django.db import models
from django.utils import timezone

class Blog(models.Model):
    body = models.TextField()
    title = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title