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
    createView,
    documrntationView,
    statistic,
    own_statistic,
    creatQuastion,
    SearchView,
)

app_name = 'quizes'

urlpatterns = [
    path('search/', SearchView, name='SearchForSmt'),#search function
    path('login/cabinet/create/<int:pk>/', creatQuastion, name='creatQuastion'),# get pk
    path('login/cabinet/ownstatic/', own_statistic, name='own_statistic'),# own stat page
    path('login/cabinet/statistic/', statistic, name='statistic'),# stat page
    path('documentation/', documrntationView, name='doc'),# help page
    path('login/cabinet/create/', createView, name="createView"),# create quiz
    path('login/', loginPage, name='log-in-view'),# log in url
    path("sightup/", sightup, name="sightup-view"),# sight up url
    path('login/cabinet/', cabinet, name='cabinet-view'),# account url
    path("logout/", logoutUser, name="logoutUser-vew"),# log out function
    path('', QuizListView.as_view(), name='main-view'),# main page
    path('<pk>/', quiz_view, name='quiz-view'),# get pk
    path('<pk>/save/', save_quiz_view, name='save-view'),#save function
    path('<pk>/data/', quiz_data_view, name='quiz-data-view'),# get data
]