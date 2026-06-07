from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Membership(models.Model):
    plan_name = models.CharField(max_length=50)
    price = models.IntegerField()
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.plan_name