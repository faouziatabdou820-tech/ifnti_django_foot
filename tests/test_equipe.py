from tournoi.models import Equipe


def test_une_equipe_a_un_nom_et_equipe(bd):
    equipe = Equipe.objects.create(nom = "les lion",promo = "L1")
    assert equipe.nom
    assert equipe.promo
    
