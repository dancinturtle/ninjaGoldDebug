from django.shortcuts import render, redirect
import random, datetime

def index(request):
    if 'totalgold' not in request.session:
        request.session['totalgold'] = [0]
        request.session['journal'] = []
    
    context = {"total":request.session['totalgold'][-1]}

    return render(request, "goldGame/index.html", context) #error added request

def process_money(request): #error process needs to match process_money
    time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
    buildings = {'farm': [10,20], 'cave': [5,10], 'house':[2,5], 'casino':[-50, 50]}
    if request.method == "POST":
        
        building = request.POST['building']
        print building
        randomNum = random.randint(buildings[building][0], buildings[building][1])
        print randomNum
        print request.session['totalgold']
        temporaryTotalGold = request.session['totalgold'][0]
        print temporaryTotalGold
        temporaryTotalGold += randomNum
        print temporaryTotalGold
        print int(temporaryTotalGold)

        # request.session['totalgold'] = int(temporaryTotalGold)

        # request.session['totalgold'] = temporaryTotalGold

        # request.session['totalgold'].append(request.session['totalgold'][-1] + randomNum)
        # print request.session['totalgold']

        # if(randomNum < 0):
        #     request.session['journal'].append("Entered a casino and lost {} gold...Ouch. {}".format(-randomNum, time))
    
        # else :
        #     request.session['journal'].append("Earned {} gold from the {}! {}".format(randomNum, building, time))
    
    return redirect('/')

def reset(request):
    request.session['totalgold'] = [0] #error clear wasn't working
    request.session['journal'] = [] #error clear wasn't working "object has no attribute 'upper'"
    return redirect('/')