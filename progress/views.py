from django.shortcuts import render, redirect
from .models import Progress

def progress_list(request):

    if request.method == 'POST':
        date = request.POST['date']
        weight = request.POST['weight']
        height = request.POST['height']
        body_fat = request.POST.get('body_fat')

        Progress.objects.create(
            date=date,
            weight=weight,
            height=height,
            body_fat=body_fat
        )

        return redirect('progress_list')

    records = Progress.objects.all()

    return render(
        request,
        'progress/progress_list.html',
        {'records': records}
    )