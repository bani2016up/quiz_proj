from django.db import models
import random



class Quiz(models.Model): # Quiz model
    
    DIFF_CHOICES = ( # options
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
    )
    
    name = models.CharField(max_length=120)#title
    topic = models.CharField(max_length=120)#what is this thimg about
    number_of_questions = models.IntegerField()#amout of quastins int the quiz
    time = models.IntegerField(help_text="duration of the quiz in minutes")#amout of time given to solve quiz
    required_score_to_pass = models.IntegerField(help_text="required score in %")#required score to pass
    difficluty = models.CharField(max_length=6, choices=DIFF_CHOICES)#uses DIFF_CHOICES

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Quizes'