from django.db import models
from datetime import date

# Create your models here.
class TarefaBD(models.Model):
    conteudo = models.CharField(max_length=1000)
    data=date.today()

    def __str__(self):
        return str(self.id)