from django.shortcuts import render


def tecnologias(request):
    return render(request, 'tecnologiaapp/tecnologia.html')
