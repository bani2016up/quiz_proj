from django.db import models
from django.db.models.deletion import CASCADE
from quizes.models import *
from django.contrib.auth.models import User


class Result(models.Model):# result model
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz')#describes wich result it is(quiz)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='results')#describes wich result it is(user)
    score = models.FloatField()#wich score user had
    
    def __str__(self):
        return str(self.pk)
    
