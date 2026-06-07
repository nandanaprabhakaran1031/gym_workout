from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Accounts
    path('', include('accounts.urls')),

    # Gym App
    path('', include('gymapp.urls')),

    # Memberships
    path('memberships/', include('memberships.urls')),

    #Workouts
    path('workouts/', include('workouts.urls')),

    #Contact
    path('contact/', include('contact.urls')),

    #Trainers
    path('trainers/', include('trainers.urls')),

    #Bmi
    path('bmi/', include('bmi.urls')),

    #Progress
    path('progress/', include('progress.urls')),
]