from django.db import models  # noqa: F401


class Equipe(models.Model):
    nom = models.CharField(max_length=20,unique=True)
    promo = models.CharField(max_length=10)
    score = models.PositiveSmallIntegerField()
    
    
    
    class Meta:
        ordering = ["promo"]
    
    
    def __str__(self):
        return f"{self.nom : self.score}"

    
    
    
    
    
    

        