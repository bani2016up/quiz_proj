from django.db import models
from django.db.models.deletion import CASCADE
from quizes.models import *
from django.contrib.auth.models import User


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()
    
    def __str__(self):
        return str(self.pk)
    
# user: qTasjhn32lej7dxjNB
# password: mhSnukdFghr734oj6lk987