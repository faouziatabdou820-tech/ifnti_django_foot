from tournoi.models import Equipe
import pytest


def test_une_equipe_a_un_nom_et_equipe(bd):
    equipe = Equipe.objects.create(nom = "les lion",promo = "L1")
    assert equipe.nom
    assert equipe.promo
    assert equipe.score
    
    
    
def test_score_inferieur_a_zero():
    equipe = Equipe.objects.create(nom = "SARA FC",promo = "L1",score = -1)
    if(pytest.raises(Exception)):
        print("PASSED .....")
    else :
        print("FAILED.....")
        
        

def test_equipe_ayant_meme_nom():
    equipe = Equipe.objects.create(nom = "les lion",promo = "L1",score = 2)
    if(pytest.raises(Exception)):
            print("PASSED .....")
    else :
            print("FAILED.....")
            
        
