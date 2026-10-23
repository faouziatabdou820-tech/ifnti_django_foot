from unicodedata import name

from django.urls import path  # noqa: F401

from . import views  # noqa: F401

app_name = "tournoi"

urlpatterns = [
    path("/matchs",views.liste_matchs,name="liste_matchs"),
    path("/equipes",views.liste_equipes,name = "liste_equipes"),
    path("/equipes/<int:pk>",views.detail_equipe,name = "detail_equipe"),
    path("/matchs/<int:pk>",views.detail_match,name = "detail_match"),


    
]
