
from django.contrib import admin
from django.urls import path


from quizz.views import index,  quizz , signin , signup ,  deconnection, start_quizz , connection , resultat

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', index , name='index'),
  path('quizz', quizz , name='quizz'),
  path('start-quizz', start_quizz , name='start_quizz'),
  path('signin', signin , name='signin'),
  path('signup', signup , name='signup'),
  path('deconnection', deconnection , name='deconnection'),
  path('connection', connection , name='connection'),
  path('resultat', resultat , name='resultat')

  ] # le nom de url chage peut donc g mi avec un - et pas _ comme ca ca fait plus jolie mais faut pas oublier a l'avenir va dans base.

from django.contrib import admin
from django.urls import path