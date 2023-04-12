from django.shortcuts import render

def proyecto(request):
    return render(request, "proyecto/proyecto.html")
