from django.db import models  # noqa: F401


class Equipe(models.Model):
    nom = models.CharField(max_length=20,unique=True)
    promo = models.CharField(max_length=10)
    
    class Meta:
            ordering = ["promo"]
        
  
  
  
class Match(models.Model):
    equipe_visiteuse = models.ForeignKey(Equipe, on_delete=models.CASCADE,related_name="matchs_exterieur")  
    equipe_domicile = models.ForeignKey(Equipe, on_delete=models.CASCADE,related_name="matchs_domicile")

    date = models.DateField()
    score_visiteur = models.PositiveSmallIntegerField(default=None)
    score_domicile = models.PositiveSmallIntegerField(default=None)
    #la referrence de equipe
    
    
    
     
    
    def __str__(self):
        return f"{self.score_domicile} - { self.score_visiteur}"

    
    
    
    
    
    
    

        