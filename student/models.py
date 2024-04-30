from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Record(models.Model):
    description = models.TextField()
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    remark = models.TextField(default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    file_upload = models.FileField(upload_to="uploads/", null=True, blank=True)
    score = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self) -> str:
        return self.title.title()


class Notification(models.Model):
    description = models.TextField()
    user = models.ForeignKey(User, models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.user.username}'s notifcation {self.created_at.now()}"
