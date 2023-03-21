from django.contrib import admin
from quizz.models import Partie
# Register your models here.
# ici comme tu peut le voir on enregistre le model dans application 
# comme ca on pourra le voir dans /admin
# pour ce faire on utilise la ligne 1 (l'importation de admin)

admin.site.register(Partie)