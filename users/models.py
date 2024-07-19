from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    """Profile model
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='profile_pics/default.jpg', upload_to='profile_pics')

    # We might want to resize images using AWS lambda function

    def __repr__(self):
        """Profile's literal representation
        """
        return f"{self.user.username}'s Profile"
