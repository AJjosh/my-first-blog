from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):  #models.Model mean that this is a Django object and should be saved in a Database
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # The properties are defined and also defines the type of each field
    title = models.CharField(max_length=2000)
    text =models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title
