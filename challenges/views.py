from django.shortcuts import render
from django.http import Http404 ,HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Finish Django course",
    "february": "Finish Django course",
    "march": "Run 30 minutes a day",
    "april": "Read 30 minutes a day",
    "may": "Learn a new language",
    "june": "Finish Django course",
    "july": "Finish Django course",
    "august": "Finish Django course",
    "september": "Finish Django course",
    "october": "Finish Django course",
    "november": "Finish Django course",
    "december": None

}
    
# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html",{
        "months": months
    })

def monthly_challenge_by_number(request,month):
    months= list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge",args=[redirect_month])#/challenge/january
    return HttpResponseRedirect(redirect_path)



def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
  
    except:
        raise Http404()
   