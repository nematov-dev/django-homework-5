from django.db import models

class VideoModel(models.Model):
    name = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"

