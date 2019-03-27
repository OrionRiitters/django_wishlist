from django.db import models

# Create your models here.

class Place(models.Model):
    """
    This model is created to store a location and whether or not it has been visited.
    """
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.name}, visited? {self.visited}'
