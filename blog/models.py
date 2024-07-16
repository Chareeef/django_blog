from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    """Post model
    """

    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        """Get a specific post's URL
        """
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __repr__(self):
        """Post representation
        """
        return f'Post: "{self.title}"'
