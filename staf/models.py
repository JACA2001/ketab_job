from django.db import models
from users.models import User

class Staf(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    est_date = models.PositiveBigIntegerField(null=True, blank=True)
    ville = models.CharField(max_length=150, null=True, blank=True)
    province = models.CharField(max_length=150, null=True, blank=True)

    # La méthode __str__ doit être indéterminée à l'intérieur de la classe
    def __str__(self):
        return self.name
