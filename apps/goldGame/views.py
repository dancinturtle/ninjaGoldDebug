# from django.shortcuts import render, redirect
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import random, datetime, time

def index(request):
    if 'totalgold' not in request.session:
        request.session['totalgold'] = [0]
        request.session['journal'] = []

    context = {"total":request.session['totalgold'][-1]}

    return render(request,"goldGame/index.html", context)
    # return render("/process_money", context)

def process(request):
    time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
    buildings = {'farm': [10,20], 'cave': [5,10], 'house':[2,5], 'casino':[-50, 50]}
    if request.method == "POST":

        # building = request.POST['Building']
        building = request.POST['building']

        randomNum = random.randint(buildings[building][0], buildings[building][1])

        request.session['totalgold'].append(request.session['totalgold'][-1] + randomNum)
        request.session.modified = True

        if(randomNum < 0):
            request.session['journal'].append("Entered a casino and lost {} gold...Ouch. {}".format(-randomNum, time))
            request.session.modified = True
        else :
            request.session['journal'].append("Earned {} gold from the {}! {}".format(randomNum, building, time))
            request.session.modified = True

    return redirect('/')

def reset(request):
    # request.session['totalgold'].clear()
    # request.session['journal'].clear()
    request.session['totalgold'] = [0]
    request.session['journal'] = []
    request.session.modified = True
    return redirect('/')
