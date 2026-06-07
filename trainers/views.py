from django.shortcuts import render 
from .models import Trainer 

def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(
        request,
        'trainers/trainer_list.html',
        {'trainers': trainers}
    )