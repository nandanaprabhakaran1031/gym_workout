from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Accounts
    path('', include('accounts.urls')),

    # Gym App
    path('', include('gymapp.urls')),

    # Memberships
    path('memberships/', include('memberships.urls')),

    # Workouts
    path('workouts/', include('workouts.urls')),

    # Contact
    path('contact/', include('contact.urls')),

    # Trainers
    path('trainers/', include('trainers.urls')),

    # BMI
    path('bmi/', include('bmi.urls')),

    # Progress
    path('progress/', include('progress.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )