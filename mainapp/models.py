from django.db import models
from .validators import validate_file_size, validate_file_extensions
from django.contrib.auth.models import User

# Create your models here.
class MediaFile(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('photo', 'Photo'),
        ('video', 'Video'),
    ]

    title = models.CharField(max_length=100)
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPE_CHOICES)
    file = models.FileField(upload_to='uploads/', validators=[validate_file_size, validate_file_extensions])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title