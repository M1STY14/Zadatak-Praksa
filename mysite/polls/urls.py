from django.urls import path
#od trenutnog foldera importirati views modul
from . import views
#obavezno lowercase
#URLConf

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    #/polls/5/
    #'name' vrijednost je pozvana od strane {% url %} template tag
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    #/polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    #/polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
