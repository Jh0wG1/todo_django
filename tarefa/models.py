from django.db import models

# Create your models here.
class TarefaBD(models.Model):
    conteudo = models.CharField(max_length=1000)
    data=models.DateField(auto_created=True)

    def __str__(self):
        return str(self.id)