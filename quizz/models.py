from django.db import models
# ajou du model User
from django.contrib.auth.models import User
# ici on cree les table pour la base de donner et ca les rentrera automatiquement (enfin presque)

# on cree une class qui herite de model (donc d'une table de db)
class Partie(models.Model):
  # on cree un champ qui recoi le user dans l'integraliter et il y a que 1 user par parti et que 1 parti par user 
  # on pourra changer si on evolu le jeux plus tard

  # si tu vois je les ajouter a OneToOneField en parametre pour lui dire que le chan c'est ca
  # g mi cascade ca veux dire que si on efface le user alors la parti aussi s'efface
  # va dans admin.py
  user = models.OneToOneField(User, on_delete=models.CASCADE) 
  points = models.IntegerField(default=0) # c'est pour un int (un nombre entier) , j'ai mi par default 0 (et g du refaire makemigration et migrate...) 
  numquestion = models.IntegerField(default=1)