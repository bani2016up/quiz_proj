import django
from django.db.models.query import QuerySet
from django.db.models.sql.query import Query
from django.http.request import QueryDict
from django.shortcuts import render, redirect
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
from questions.models import Question, Answer
from results.models import Result
from django.contrib.auth.forms import UserCreationForm, UserModel
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import *


def documrntationView(request):
    data ={}
    return render(request, 'quizes/documrntationView.html')

@login_required(login_url='/login/')
def statistic(request):
    users = get_user_model().objects.all()
    result = Result.objects.all()
    result_count = result.count()   
    user_get_id = request.user
    user_id = user_get_id.id 
    user_data =   Result.objects.filter(user__pk=user_id)   
    data = {'allusers': users,
            'result_count':result_count,
            'result': user_data
            }    
    return render(request, 'quizes/statistic.html', data)   


@login_required(login_url='/login/')
def own_statistic(request):
    user_get_id = request.user
    user_id = user_get_id.id
    result = Result.objects.filter(user__pk=user_id)
    result_count = result.count()
    
    
    data = {'result_count' : result_count}
    return render(request, 'quizes/own_statistics.html', data)

@login_required(login_url='/login/')
def cabinet(request):
    data ={}
    return render(request, 'quizes/cabinet.html', data)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/login/cabinet/')
        else:
            messages.info(request, 'username or pssword is wrong')
    data = {}
    return render(request, 'quizes/login.html', data)
@login_required(login_url='/login/')
def logoutUser(request):
    logout(request)
    return redirect('/')

def sightup(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Acount was created' + user)
            return redirect('/login/')
        
        
    data = {'form': form}
    return render(request, 'quizes/sightup.html', data)

class QuizListView(ListView):
    model = Quiz 
    template_name = 'quizes/main.html'
    
@login_required(login_url='/login/')
def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quizes/quiz.html', {'obj': quiz})
@login_required(login_url='/login/')
def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })
@login_required(login_url='/login/')
def save_quiz_view(request, pk):
    if request.is_ajax():
        questions = []
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(text=k)
            questions.append(question)
        print(questions)

        
        
        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        multiplier = 100 / quiz.number_of_questions
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.text)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text

                results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                results.append({str(q): 'not answered'})
            
        score_ = score * multiplier
        Result.objects.create(quiz=quiz, user=user, score=score_)
        
        if score_ >= quiz.required_score_to_pass:
            return JsonResponse({'passed': True, 'score': score_, 'results': results})
        else:
            return JsonResponse({'passed': False, 'score': score_, 'results': results})
        
@login_required(login_url='/login/')    
def createView(request):
    
    form = QuizForm()
    if request.method == 'POST':
        print('Posting....*', request.POST)
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect(f'/login/cabinet/create/{form.instance.pk}/')
    context ={'form': form}
    return render(request, "quizes/createviews.html", context)

@login_required(login_url='/login/') 
def creatQuastion(request, pk):
    form = AnswearForm()
    form2 = QuastionrForm()
    if request.method == 'POST':
        print('Posting....*', request.POST)
        form = AnswearForm(request.POST)
        form2 = QuastionrForm(request.POST)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return redirect('/login/cabinet/')
        
    
    context = {'pk' : pk, 'form': form, 'form2' : form2}
    return render(request, "quizes/created.html", context)

def SearchView(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        quiz = Quiz.objects.filter(name__contains=searched)
        context={
            'searched': searched,
            'quiz': quiz,
                 }
        return render(request, "quizes/search.html", context )
    else:
        context={}
        return render(request, "quizes/search.html", context )