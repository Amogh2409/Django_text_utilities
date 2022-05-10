# This file was created by me and it was not given or not created by default
from string import punctuation
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    # content = {
    #     "Data": "Youtube is best",
    #     "Roll_number": [1,2,3,4,5,6,7,8,9,10],
    #     "first_name": "Amogh",
    #     "last_name": "Saxena",
    #     "variable_name": "This is a educational video in which we are going to study about templates."

    # }

    return render(request, "textutils-2.html")
#     return HttpResponse('''<nav style="margin: 50px;"><a href="www.google.com" style="margin-right: 20px;">Google</a>
# <a href="www.facebook.com" style="margin-right: 20px;">Facebook</a>
# <a href="www.youtube.com" style="margin-right: 20px;">Youtube</a>
# <a href="www.apple.com">Apple</a></nav>''')


def removepunctuations(request):
    inputtext = request.POST.get('text', 'default')
    removepunctuations = request.POST.get('removepunctuations', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')

    if removepunctuations == "on":
        punctuations = '''!@$%^&*()_+-={}[];:><'",.?/#'''
        analyzed = ""
        for char in inputtext:
            if char not in punctuations:
                analyzed = analyzed + char

        user_text = {'Task': 'Removed Punctuations', 'analyzed_text': analyzed}
        inputtext = analyzed

    if capitalize == "on":
        analyzed = ""
        for char in inputtext:
            analyzed = analyzed + char.upper()

        user_text = {'Task': 'Capitalized', 'analyzed_text': analyzed}
        inputtext = analyzed

    if spaceremover == "on":
        analyzed = ""
        for index, char in enumerate(inputtext):
            if not (inputtext[index] == " " and inputtext[index + 1]== " "):
                analyzed = analyzed + char

        user_text = {'Task': 'Sorted', 'analyzed_text': analyzed}
        inputtext = analyzed
       
    if(removepunctuations != "on" and capitalize != "on" and spaceremover != "on"):
        return HttpResponse("You have not selected any operations !!")

    return render(request, 'analyzed.html', user_text)

    # else:
        # return HttpResponse('ERROR - YOUR TEXT HAS NOT BEEN ANALYZED')


def capitalize(request):
    return HttpResponse("capitalize")


def spaceremover(request):
    return HttpResponse("spaceremover")


def about(request):
    return HttpResponse("abouut this web page")


def home(request):
    return HttpResponse("welcome to the home page of this website")
