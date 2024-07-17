from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    prix = models.FloatField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    
      

    def __str__(self):
        return self.title

    def calculer_prix_final(self):
        
        if self.prix and self.discount:
            remise_montant = (self.discount / 100) * self.prix
            prix_final = self.prix - remise_montant
            return prix_final
        return self.prix  
