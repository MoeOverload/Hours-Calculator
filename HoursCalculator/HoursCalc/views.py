from django.shortcuts import render


def Home(request):
    return render(request, "HomePage.html")


def AddHours(request):
    return render(request, "AddHours.html")


def ViewHours(request):
    return render(request, "ViewHours.html")