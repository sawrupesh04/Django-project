from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    text = request.GET['text'] 
    textList = text.split()

    worddict = {}

    for word in textList:
        if word in worddict:
            # increase
            worddict[word]+=1
        else:
            # add a line to dictionary
            worddict[word]=1

        sortword = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'text': text, 'textList': len(textList), 'sortword': sortword})

def about(request):
    return render(request, 'about.html')