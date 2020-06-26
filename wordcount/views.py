from django.http import HttpResponse
from django.shortcuts import render
import operator

def show(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def count(request):
    wholetext = request.GET['wholetext']
    textlist = wholetext.split()

    textdictionary = {}

    for word in textlist:
        if word in textdictionary:
            textdictionary[word] +=1
        else:
            textdictionary[word] = 1

    sortdictionary = sorted(textdictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'countnow.html',{'htmlwholetext':wholetext,'htmltextcount':len(textlist),'htmltextdictionary':textdictionary,'sortdictionary':sortdictionary})
