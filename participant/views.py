from django.shortcuts import render
from django.http import HttpResponse
from .models import participant
# Create your views here.
from django import forms
from datetime import datetime
from random import randint

#def index(request):
#   return HttpResponse("Hello, world.")

def index(request):
    participants = participant.objects.all()
    errors = []
    winner = []
    form = {}
    if request.POST: 
        form['nickname'] = request.POST.get('nickname')
        if 'reg' in request.POST:
            if not form['nickname']:
                errors.append('Заполните имя.')
            if True == bool(participant.objects.filter(nickname=form['nickname'])): 
                errors.append('Уже зарегистрирован.')
            if not errors:
                participant.objects.create(nickname=form['nickname'], reg_date=datetime.now())
                
        elif 'del' in request.POST:
            if not form['nickname']:
                errors.append('Заполните имя.')
            if False == bool(participant.objects.filter(nickname=form['nickname'])): 
                errors.append('Пользователь не найден.')
            if not errors: 
                participant.objects.filter(nickname=form['nickname']).delete()
                
        elif 'win' in request.POST:
            count=participant.objects.all().count()
            i=0
            ranins=[]
            while i<3:
                ranin=randint(1, count-1)
                if ranin in ranins:
                    continue
                else:
                    i+=1
                    ranins.append(ranin)
                
            winner=[participant.objects.all()[ranins[0]], participant.objects.all()[ranins[1]], participant.objects.all()[ranins[2]]]
            #winner=[randint(1, count), randint(1, count), randint(1, count)]
                
    parlen = participant.objects.all().count()
    return render(request, 'participant/index.html', {'participant_len': parlen, 'participants': participants,'errors': errors, 'form':form, 'winner': winner})

