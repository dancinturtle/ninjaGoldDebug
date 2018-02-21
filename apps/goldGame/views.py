from django.shortcuts import render, redirect
import random, datetime

def index(request):
    if 'totalgold' not in request.session:
        request.session['totalgold'] = [0]
        request.session['journal'] = []
    print request.session['totalgold']
    context = {"total":request.session['totalgold'][-1]}
    return render(request, "goldGame/index.html", context)

def process(request):
    time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
    buildings = {'farm': [10,20], 'cave': [5,10], 'house':[2,5], 'casino':[-50, 50]}

    if request.method == "POST":
        building = request.POST['building']
        randomNum = random.randint(buildings[building][0], buildings[building][1])
        request.session['totalgold'].append(request.session['totalgold'][-1] + randomNum)

        if(randomNum < 0):
            request.session['journal'].append("Entered a casino and lost {} gold...Ouch. {}".format(-randomNum, time))

        else :
            request.session['journal'].append("Earned {} gold from the {}! {}".format(randomNum, building, time))

    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
