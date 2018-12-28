from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
# '/' - survey
def index(request):

    return render(request, 'index.html')

# '/process' - post from the from and collect data
def process(request):
    if request.method == "POST":
        if len(request.POST['name']) <= 1:
            return redirect('/')
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']

    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1
    
    return redirect('/result')

# '/result' - display form data
def result(request):

    data = {
        'name'      :   request.session['name'],
        'location'  :   request.session['location'],
        'language'  :   request.session['language'],
        'comment'   :   request.session['comment'],
        'count'     :   request.session['counter']
    }

    return render(request, 'result.html', data)
