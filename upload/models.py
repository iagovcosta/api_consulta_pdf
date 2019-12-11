from django.db import models

# Create your models here.
class File(models.Model):
    file = models.FileField(blank=False, null=False)
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title