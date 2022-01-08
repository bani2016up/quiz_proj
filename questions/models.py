from django.db import models
from quizes.models import Quiz

class Question(models.Model):#quastion model
    text = models.CharField(max_length=200)#content of Question
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)#related to.....
    created = models.DateTimeField(auto_now_add=True)# was created.....
    # points = models.IntegerField() # for fuecher

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()

class Answer(models.Model):#Answer model
    text = models.CharField(max_length=200)#Answer text
    correct = models.BooleanField(default=False)#is corect true or false
    question = models.ForeignKey(Question, on_delete=models.CASCADE)#related to.....
    created = models.DateTimeField(auto_now_add=True)
    # points = models.IntegerField()# for fuecher
    
    

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"