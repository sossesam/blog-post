
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class taskDb(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title= models.CharField(max_length=25)
    description= models.CharField(max_length=50)
    post = models.CharField(max_length=500)
    date_published = models.DateTimeField(default= timezone.now)
        

    def __str__(self):
        return "%s %s"%(self.title,self.author)