from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    photo = models.ImageField(upload_to='trainers/')

    def __str__(self):
        return self.name