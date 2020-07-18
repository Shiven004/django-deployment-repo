from django.db import models
#for value in variable}from django.utils import timezone

# Create your models here.
class Topic(models.Model):

    top_name = models.CharField(max_length=256,unique=True)

    def __str__(self):
        return self.top_name

class WebPage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=264,unique=True)
    url_name = models.URLField(unique=True)

    def __str__(self):
        return self.name
        
class AccessRecord(models.Model):

    name = models.ForeignKey(WebPage,on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
