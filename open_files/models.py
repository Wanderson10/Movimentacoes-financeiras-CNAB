from django.db import models

class File(models.Model):
    
    date = models.DateField()
    type = models.CharField(max_length=10)
    cpf = models.IntegerField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.TimeField()
    value = models.CharField(max_length=10)
    store_owner = models.CharField(max_length=14)
    store_name = models.CharField(max_length=19)

    def __str__(self):
        return self.store_name  + self.value + self.store_name
