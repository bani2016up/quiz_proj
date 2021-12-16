from django.urls import path
from .views import (
    cabinet,
    QuizListView,
    loginPage,
    sightup,
    quiz_view,
    quiz_data_view,
    save_quiz_view,
    logoutUser,
    resultView,
    createView,
    quastionscreateView,
    documrntationView,
    statistic,
    own_statistic,
)

app_name = 'quizes'

urlpatterns = [
    path('login/cabinet/ownstatic/', own_statistic, name='own_statistic'),
    path('login/cabinet/statistic/', statistic, name='statistic'),
    path('documentation/', documrntationView, name='doc'),
    path('login/cabinet/create/quastion/', quastionscreateView, name="createView"),
    path('login/cabinet/create/', createView, name="Create-view"),
    path("login/cabinet/result/", resultView, name="result-View"),
    path('login/', loginPage, name='log-in-view'),
    path("sightup/", sightup, name="sightup-view"),
    path('login/cabinet/', cabinet, name='cabinet-view'),
    path("logout/", logoutUser, name="logoutUser-vew"),
    path('', QuizListView.as_view(), name='main-view'),
    path('<pk>/', quiz_view, name='quiz-view'),
    path('<pk>/save/', save_quiz_view, name='save-view'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view'),
]