from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PostIt(models.Model):
    post_title = models.CharField(max_length=100)
    post_body = models.CharField(max_length=300)
    posted_date = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title
