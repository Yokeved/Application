from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# on import le model de user
from django.contrib.auth import get_user_model
# ici on import le model Partie comme ca on puisse l'utiliser dans la page
from quizz.models import Partie


# creation d'une page
def index(request):
    return render(request, 'index.html')


from django.http import HttpResponse


def start_quizz(request):
    if str(request.user) == 'AnonymousUser':
        return redirect('signin')
    qest_ans = [{
        'question':
        'A journalist\'s source who wants to remain anonymous may speak "on" this, or even "on deep" this',
        'reponse': 'background'
    }, {
        'question': 'Hairy Himalayans herded here',
        'reponse': 'yaks'
    }, {
        'question':
        'Born in Kentucky Feb.12, 1809, Abe Lincoln lived from age 7 to 21 in this state before the move to Illinois'
    }, {
        'reponse': 'Indiana'
    }]
    # on recupere la question a afficher
    question = qest_ans[0]['question']
    # meme chose pour reponse
    reponse = qest_ans[0]['reponse']
    # list des reponses
    list_reponses = ['yaks', 'background', 'Indiana']
    # la tu appel la parti

    data = {
        'question': question,
        'reponse': reponse,
        'list_reponses': list_reponses,
        'numquestion': '1'
    }

    if request.method == "POST":
        # la tu recupere la reponse
        reponse_send = request.POST.get('radio_button')
        # la tu appel la db en creant ou cherchant
        # si elle existe deja tu met a 0
        partie, created = Partie.objects.get_or_create(user=request.user)
        if not created:
            partie.numquestion = 1
            partie.points = 0
        # ici tu implemant (Hazak)
        print(partie)
        if reponse_send == reponse:
            partie.points = 1
        else:
            partie.points = 0
        partie.numquestion = 2
        partie.save()
        # partie.update(points=new_points , numquestion=new_numquestion)
        # for object in partie:
        # object['numquestion']=new_numquestion
        # object.save()
        return redirect('quizz')
        print(reponse_send)
    return render(request, 'quizz.html', data)


def quizz(request):
    # ici on change pour ajouter un point si la reponse est juste
    qest_ans = [{
        'question':
        'A journalist\'s source who wants to remain anonymous may speak "on" this, or even "on deep" this',
        'reponse': 'background'
    }, {
        'question': 'Hairy Himalayans herded here',
        'reponse': 'yaks'
    }, {
        'question':
        'Born in Kentucky Feb.12, 1809, Abe Lincoln lived from age 7 to 21 in this state before the move to Illinois'
    }, {
        'reponse': 'Indiana'
    }]
    # on recupere la question a afficher
    question = qest_ans[0]['question']
    # meme chose pour reponse
    reponse = qest_ans[0]['reponse']
    # list des reponses
    list_reponses = ['yaks', 'background', 'Indiana']
    partie = Partie.objects.filter(user=request.user)[0]

    numquestion = partie.numquestion

    data = {
        'question': question,
        'reponse': reponse,
        'list_reponses': list_reponses,
        'numquestion': numquestion
    }
    # on l'envoie dans la page html
    if request.method == "POST":
        reponse_send = request.POST.get('radio_button')

        if reponse_send == reponse:
            partie.points = partie.points + 1

        partie.numquestion = partie.numquestion + 1
        partie.save()
        if numquestion == 10:
            return redirect('resultat')
        # faire une fonction qui redirige vert une page resulat avec le score si fin de 10eme quesions
        return redirect('quizz')
        print(reponse_send)
    return render(request, 'quizz.html', data)


def signin(request):
    if request.method == "POST":
        # ici on recuper les donne du formulaire
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


# on defini que c notre model (c'est la table de la database)
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
        # on verifi que le user n'exist pas
        else:
            # on cree une instance du new  utilisateur
            if password == password2:
                user = UserModel.objects.create_user(username, email, password)
                user.save()
                return redirect('signin')
            else:
                messages.error(request,
                               'Les mots de passe doivent être identiques')
                return redirect('signup')
            # on enregistre dans la DB
        # user.save()
        # on redirige a login

        # va dans signup page
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
  points 
    return render(request, 'resultat.html')

    """
    j'ai mi la parti d'ailleur qui est forcement cree donc il y a pas besoin de verifiee
  partie est un dictionnaire
  en 2 mot un dict c
  les valeur peut etre des list des int des dict ou des str
  on peut aussi lui passer des variable
  ta compri plus ou moin le debu?oue cv 
  dict1 ={'key': [1, 2, 'ceci est une list']}
  dict1 ={'key':dict} # la g mi le dict si dessu
  dict1 ={'key': 1} #int
  dict1 ={'key': 'value'}
  dict1 ={'key': 'value'}
  data est un dict
  maintenant pour acceder a une valeur on fait
  dict1['key'] est ca nous sort la valeur
  si on veu ajouter une valeur dans notre dict on fait
  dict1['new_key'] = new_value
  ou on peu changer justela valeur d'une Key
  dict1['new_key'] = new_new_value # mdr 
  ta compri pourquoi g recup la data de parti qui est un dict de cette maniere
   tu peu aussi faire de cette maniere
  dict1.key # et tu resort la valeur. mais defois ca marche pas
  on as pas le droi d utiliser le nom dict mdr alors fais gaff si g oublier 1
  je te met en bas de la page
  """