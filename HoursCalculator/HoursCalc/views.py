from django.shortcuts import render


def Home(request):
    return render(request, "HomePage.html")


def AddHours(request):
    return render(request, "AddHours.html")


def ViewHours(request):
    return render(request, "ViewHours.html")


def LoginUser(request):
    return render(request, "LoginPage.html")

def CreateUser(request):
    if request.method == "GET":
        return render(request, "CreateUser.html")
    elif request.method == "POST":
        Email = request.POST["Email"]
        Username = request.POST["Username"]
        Password = request.POST["Password"]
        Confirmation = request.POST["Confirmation"]
        if Password != Confirmation:
            pass
        


