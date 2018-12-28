from django.shortcuts import render, redirect
import random
import datetime

def getGold(place):
    if place == "farm":
        return random.randrange(9, 21)
    elif place == "cave":
        return random.randrange(4, 11)
    elif place == "home":
        return random.randrange(1, 6)
    elif place == "casi":
        return random.randrange(-51, 51)
    else:
        return 0

def addGold(request, place):
    gold = int(getGold(place))
    newGold = {
        'amount':   gold,
        'place':    place,
        'time':     returnTime()
    }

    activity = request.session['activities']
    activity.insert(0,newGold)
    request.session['activities'] = activity
    request.session['gold'] += gold

def returnTime():
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")

    return now_str


# Create your views here.
def index(request):

    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    
    data = {
        'gold'      :   request.session['gold'],
        'activities':   request.session['activities']
    }

    return render(request, 'index.html', data)

def process(request, place):
    addGold(request, place)

    return redirect('/')

def reset(request):
    request.session.clear()

    return redirect('/')