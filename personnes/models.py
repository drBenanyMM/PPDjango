from django.db import models

class Personne(models.Model):
    nom = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nom 
