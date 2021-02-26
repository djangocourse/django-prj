from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout


def index_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username = email, password = password)

        if user:
            login(request, user)
        else:
            return HttpResponse("Not Valid!")

    return render(request, 'panel/index.html')


def panel_view(request):
    return render(request, 'panel/teacher_panel.html')
