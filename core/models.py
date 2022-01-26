from django.db import models

# Create your models here.
class Resource(models.Model):
    """
    Model of Resource

    Attributes:
        id
        title
        url
        description
        created_at
        updated_at
    """

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    video = models.FileField(upload_to='media/videos', blank=True, max_length=255)
    document = models.FileField(upload_to='media/documents', blank=True, max_length=255)
    
    # * Metada
    class Meta:
        managed = True
        verbose_name = 'Resource'
        verbose_name_plural = 'Resources'
    
    def __str__(self):
        return self.title