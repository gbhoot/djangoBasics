from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):

    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1

    random_word = get_random_string(length=14).upper()
    print(random_word)

    data = {
        'word'  :   random_word,
        'count' :   request.session['counter']
    }

    return render(request, 'index.html', data)

def reset(request):

    del request.session['counter']

    return redirect('/random_word')