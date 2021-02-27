from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from . import models, forms

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

@login_required
def panel_view(request):
    homeworks = models.Homework.objects.all()
    if request.user.is_teacher:
        if request.method == 'POST':
            text = request.POST.get('text')
            deadline = request.POST.get('deadline')
            homework = models.Homework(text = text, deadline = deadline)
            homework.save()

        return render(request, 'panel/teacher_panel.html', context = {'homeworks':homeworks})
    else:
        return render(request, 'panel/student_panel.html', context = {'homeworks':homeworks})

@login_required
def video_view(request):
    form = forms.VideoForm()
    vids = models.Video.objects.all()
    if request.user.is_teacher:
        if request.method == 'POST':
            form = forms.VideoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()

        return render(request, 'panel/teacher_vid.html', context = {'vids':vids, 'form':form})
    else:
        return render(request, 'panel/student_vid.html', context = {'vids':vids})
