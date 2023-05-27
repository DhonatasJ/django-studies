from django.db import models

class Topic(models.Model):
    """"Anote"""
    text = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
