import datetime

from django.db import models
from django.utils import timezone



# Question model

class Question(models.Model):
    q_text = models.CharField(max_length=200)
    p_date = models.DateTimeField('date published')
    def __str__(self):
         return self.q_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
# Choice model

class Choice(models.Model):
    q = models.ForeignKey(Question, on_delete=models.CASCADE)
    c_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
         return self.c_text


