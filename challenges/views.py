from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def monthly_challenge_by_number(request,month):
    return HttpResponse(month)

def monthly_challenge(request,month):
    challenge_text:None
    if month == "january":
        challenge_text = "Finish Django course"
    elif month == "february":
        challenge_text = "Eat more vegetables"
    elif month == "march":
        challenge_text = "Run 30 minutes a day"
    elif month == "april":
        challenge_text = "Read 30 minutes a day"
    elif month == "may":
        challenge_text = "Learn a new language"
    elif month == "june":
        challenge_text = "Do not skip gym on weekdays"
    elif month == "july":
        challenge_text = "Sleep earlier"
    elif month == "august":
        challenge_text = "Eat more vegetables"
    elif month == "september":
        challenge_text = "Eat more vegetables"
    elif month == "october":
        challenge_text = "Eat more vegetables"
    elif month == "november":
        challenge_text = "Eat more vegetables"
    elif month == "dicember":
        challenge_text = "Eat more vegetables"
    else:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge_text)