from tournoi.models import Equipe
from tournoi.models import Match
import pytest
from django.db import models

def test_une_equipe_a_un_nom_et_equipe(db):
    equipe = Equipe.objects.create(nom = "les lion",promo = "L1")
    equipe1 = Equipe.objects.create(nom = "les lion",promo = "L2")
    
    assert equipe.nom
    assert equipe.promo
  
    
    
    
def test_score_inferieur_a_zero(db):
    match = Match.objects.create(equipe_visiteur = "MADRID",date = "02-02-2025",score = -1)
    if(match.score_domicile < 0 or match.score_visiteur < 0):
        print("PASSED .....")
    else :
        print("FAILED.....")
        
        

def test_equipe_ayant_meme_nom(db):
    equipe = Equipe.objects.create(nom = "les lion",promo = "L1",score = 2)
    if(pytest.raises(Exception)):
            print("PASSED .....")
    else :
            print("FAILED.....")
            
            
def test_match_non_jouer_score_inconnu(db):
    match = Match()
    if match.score_visiteur == None and match.score_domicile == None : 
        assert match
        return "Iconnu"
        
        
