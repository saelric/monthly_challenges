from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "Finish Django course",
    "february": "Eat more vegetables",
    "march": "Run 30 minutes a day",
    "april": "Read 30 minutes a day",
    "may": "Learn a new language",
    "june": "Do not skip gym on weekdays",
    "july": "Sleep earlier",
    "august": "Eat more vegetables",
    "september": "Eat more vegetables",
    "october": "Eat more vegetables",
    "november": "Eat more vegetables",
    "december": "Eat more vegetables"

}
    
# Create your views here.

def monthly_challenge_by_number(request,month):
    months= list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month")
    
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")   
   