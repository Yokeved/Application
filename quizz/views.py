from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth import get_user_model
from quizz.models import Partie
from django.http import HttpResponse
import json
import random


def index(request):
    return render(request, 'index.html')


def start_quizz(request):
    if str(request.user) == 'AnonymousUser':
        return redirect('signin')
    
    with open ("quizz/data.json") as f:
        data = json.load(f)
    nbrandom = random.randint(0,len(data)-1)
    question_dict = data[nbrandom]
    question_text = question_dict["question_text"]
    options = question_dict["options"]
    answer = question_dict["answer"]

    data = {
        'question_text': question_text,
        'options': options,
        'answer': answer,
        'numquestion': 1
    }
   

    if request.method == "POST":
        reponse_send = request.POST.get('radio_button')
        right_reponse = request.POST.get('right_reponse')

        
        partie, created = Partie.objects.get_or_create(user=request.user)
        if not created:
            partie.numquestion = 1
            partie.points = 0
        print(partie)
        if reponse_send == right_reponse:
            partie.points = partie.points + 1
        else:
            partie.points = 0
        partie.numquestion = 2
        partie.save()

        return redirect('quizz')
    return render(request, 'quizz.html', data)


def quizz(request):
    with open ("quizz/data.json") as f:
        data = json.load(f)
    nbrandom = random.randint(0,len(data)-1)
    question_dict = data[nbrandom]
    question_text = question_dict["question_text"]
    options = question_dict["options"]
    answer = question_dict["answer"]

    partie = Partie.objects.filter(user=request.user)[0]

    numquestion = partie.numquestion

    data = {
        'question_text': question_text,
        'options': options,
        'answer': answer,
        'numquestion': numquestion
    }
    if request.method == "POST":
        reponse_send = request.POST.get('radio_button')
        right_reponse = request.POST.get('right_reponse')

        if reponse_send == right_reponse:
            partie.points = partie.points + 1

        partie.numquestion = partie.numquestion + 1
        partie.save()
        if numquestion == 10:
            return redirect('resultat')
        print(reponse_send)
        return redirect('quizz')

    return render(request, 'quizz.html', data)


def signin(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        username = username.lower()
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('start_quizz')
        else:
            messages.error(
                request,
                "L'utilisateur n'existe pas ou les identifiants sont incorrects"
            )
    else:
        print('get')
    return render(request, 'signin.html')

UserModel = get_user_model()


def signup(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        username = username.lower()

        if UserModel.objects.filter(username=username).exists():
            messages.error(request, 'Ce nom ou adresse email existe déjà ')
            return redirect('signup')
        else:
            if password == password2:
                user = UserModel.objects.create_user(username, email, password)
                user.save()
                return redirect('signin')
            else:
                messages.error(request,
                               'Les mots de passe doivent être identiques')
                return redirect('signup')
    else:
        return render(request, 'signup.html')


def deconnection(request):
    if request.method == "GET":
        logout(request)
        return redirect('signin')
    return render(request, 'deconnection.html')


def connection(request):
    return render(request, 'connection.html')


def resultat(request):
    partie = Partie.objects.filter(user=request.user)[0]
    points = partie.points
    data = {
        'points': points,
    }
    return render(request, 'resultat.html', data)
