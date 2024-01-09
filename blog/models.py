from django.db import models
from django.urls import reverse
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Set when the instance is created
    
    def __str__(self):
        return self.title
 
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})