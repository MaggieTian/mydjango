from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
    question_txt=models.CharField(max_length=200)
    pub_data=models.DateField('date published')



class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_txt = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


