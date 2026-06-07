from django.shortcuts import render
from trainers.models import Trainer
from memberships.models import Membership

def home(request):
    trainers = Trainer.objects.all()
    memberships = Membership.objects.all()

    return render(request, 'gymapp/home.html', {
        'trainers': trainers,
        'memberships': memberships,
    })