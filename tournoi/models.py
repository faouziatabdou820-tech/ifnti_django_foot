from django.db import models  # noqa: F401


class Equipe(models.Model):
    nom = models.CharField(max_length=20,unique=True)
    promo = models.CharField(max_length=10)
    equipe= models.ManyToManyField(Equipe,on_delete = models.PROTECT,related_name=equipes)
    
    class Meta:
            ordering = ["promo"]
        
  
  
  
class Match(models.Model):
    equipe_visiteuse = models.CharField(max_length=100)
    date = models.DateField()
    score_visiteur = models.PositiveSmallIntegerField(default="ICONNU")
    score_domicile = models.PositiveSmallIntegerField(default="ICONNU")
    #la referrence de equipe
    
    
    
     
    
    def __str__(self):
        return f"{self.nom : self.score_domicile - self.score_visiteur}"

    
    
    
    
    
    
    

        