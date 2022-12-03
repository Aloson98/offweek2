from django.db import models

# Create your models here.

class news(models.Model):
    CATEGORY = (
        ('HEALTH', 'HEALTH'),
        ('EDUCATION', 'EDUCATION'),
    )

    title          = models.CharField(max_length=120)
    author         = models.CharField(max_length=40)
    category       = models.CharField(max_length=80, choices=CATEGORY)
    content        = models.TextField()
    content_image  = models.ImageField(blank=True, upload_to='media/')

    def __str__(self):
        return self.title