from django.db import models

class Progress(models.Model):
    date = models.DateField()
    weight = models.FloatField()
    height = models.FloatField()
    body_fat = models.FloatField(null=True, blank=True)

    def bmi(self):
        return self.weight / ((self.height / 100) ** 2)

    def __str__(self):
        return f"{self.date} - {self.weight} kg"