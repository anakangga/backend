from django.db import models
from user.models import Pengguna

# Create your models here.
class VideoCustomer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Pengguna, on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title
    
class InterpreterVideo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Pengguna, on_delete=models.CASCADE, related_name='interpreter_videos')
    video = models.FileField(upload_to='videos/')
    video_customer = models.ForeignKey(VideoCustomer, on_delete=models.CASCADE, related_name='interpreter_videos')

    def __str__(self):
        return self.title