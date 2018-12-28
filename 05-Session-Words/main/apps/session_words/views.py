from django.shortcuts import render, redirect
import datetime

# Create your views here.
def index(request):

    if 'words' not in request.session:
        request.session['words'] = []
    
    data = {
        'words' :   request.session['words']
    }

    print("DATATAAAAA ZIZZ", data)

    return render(request, 'index.html', data)

def add(request):
    newWord = {}

    print

    if request.method == "POST":
        if len(request.POST['word']) < 2:
            return redirect('/')
        if 'checker' not in request.POST:
            newWord['checker'] = False
        else:
            newWord['checker'] = True
        newWord['word'] = request.POST['word']
        newWord['color'] = request.POST['color']
        newWord['timestamp'] = datetime.datetime.now().strftime("%b %d, %Y at %H:%M %p")

    words = request.session['words']
    words.insert(0,newWord)
    request.session['words'] = words

    # print(words)
    print(request.session['words'])
    
    return redirect('/')

def clear(request):
    request.session.clear()

    return redirect('/')