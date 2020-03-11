from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html', {'hithere':'This is me'})

def eggs(request):
    return HttpResponse('<h1>Eggs are great</h1>')

def count(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    wordlist = fulltext.split()

    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1

    worddictionary.items() # convert to list
    sortedwords = sorted(worddictionary.items(), key = operator.itemgetter(1),  reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})

def about(request):

    return render(request, 'about.html', {'strongpassionatewords':'This is a challenge page from nick walter tutorial.'})