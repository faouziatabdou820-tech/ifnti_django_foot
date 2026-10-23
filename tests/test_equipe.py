from xmlrpc import client

from tournoi.models import Equipe ,Match

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
    assert match.score_domicile is None
    assert match.score_visiteur is None
 

@pytest.fixture        
def test_recuperee_tous_les_matchs(
    match_l3_et_l2,
    client,
    match_l1__et_l3,
):

    response = client.get("/matchs")
    assert response.status_code == 200
    assert "25 Octobre 2026" in response.text
    assert "30 Octobre 2026" in response.text



def test_recuperee_un_equipe(client,equipe_1):
    response = client.get("/equipes/{equipe_1.id}")
    assert response.status_code == 200
    assert "les lion" in response.text
    assert "l1" in response.text
    
#def test_recuperer_un_match():
    
    
    
    