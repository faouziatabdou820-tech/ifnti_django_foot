from tournoi.models import Equipe
from tournoi.models import Match
import pytest
from django.db import models

def test_une_equipe_a_un_nom_et_equipe(db):
    equipe = Equipe.objects.create(nom = "les lion",promo = "L1")    
    assert equipe.nom
    assert equipe.promo
        
        

def test_equipe_ayant_meme_nom(db):
    equipe = Equipe.objects.create(nom = "les lion",promo = "L1")
    with pytest.raises(Exception):
        equipe2 = Equipe.objects.create(nom = "les lion",promo = "L2")
   
            
            
def test_match_non_jouer_score_inconnu(db):
    match = Match()
    assert match.score is None
       
        
        
