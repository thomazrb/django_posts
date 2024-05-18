from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        if len(self.text) > 20:
            return f'{self.text[:20]} (...)'
        else:
            return self.text