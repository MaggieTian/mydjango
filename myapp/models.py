from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class QuestionTian(models.Model):

    question_txt=models.CharField(max_length=200)
    pub_data=models.DateField('date published')

    def __str__(self):
        return self.question_txt

class Choice(models.Model):

    question = models.ForeignKey(QuestionTian)
    choice_txt = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_txt


