from django.forms import ModelForm
from .models import Quiz
from questions.models import *

class QuizForm(ModelForm):
    
    class Meta:
        model = Quiz
        fields = '__all__'
class AnswearForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['text',
                  'correct',
                  'question']

class QuastionrForm(ModelForm):
    class Meta:
        model = Question
        fields = ['text',
                  'quiz',]