from django.urls import path
from .views import (
    QuizListView,
    loginPage,
    sightup,
    quiz_view,
    quiz_data_view,
    save_quiz_view
)

app_name = 'quizes'

urlpatterns = [
    path('login/', loginPage, name='log-in-view'),
    path("sightup/", sightup, name="sightup-view"),
    path('', QuizListView.as_view(), name='main-view'),
    path('<pk>/', quiz_view, name='quiz-view'),
    path('<pk>/save/', save_quiz_view, name='save-view'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view'),
]