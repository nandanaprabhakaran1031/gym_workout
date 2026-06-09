from django.shortcuts import render


def bmi_calculator(request):

    bmi = None
    status = None

    if request.method == 'POST':

        weight = float(request.POST['weight'])
        height = float(request.POST['height']) / 100

        bmi = round(weight / (height ** 2), 2)

        if bmi < 18.5:
            status = "Underweight"

        elif bmi < 25:
            status = "Normal"

        else:
            status = "Overweight"

    return render(
        request,
        'bmi/bmi.html',
        {
            'bmi': bmi,
            'status': status,
        }
    )