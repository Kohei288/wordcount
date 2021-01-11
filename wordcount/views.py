from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordsList = fulltext.split()
    words_Dictionary = {}

    for word in wordsList:
        if word in words_Dictionary:
            words_Dictionary[word] += 1
        else:
            words_Dictionary[word] = 1

    sortedWords = sorted(words_Dictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordsList), 'words_Dictionary': sortedWords})

def about(request):
    return render(request, 'about.html')
