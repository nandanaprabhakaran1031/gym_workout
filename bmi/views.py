from django.shortcuts import render 

def bmi_calculator(request):
    bmi = None

    if request.method == 'POST':
        weight = float(request.POST['weight'])
        height = float(request.POST['height'])

        bmi = weight / (height ** 2)

    return render(request, 'bmi/bmi.html', {'bmi': bmi})