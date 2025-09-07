from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challange={
    "january":"<h1>Start your Goal</h2>",
    "february":"Learn Django",
    "march":"Learn REST",
    "april":"Learn Testing",
    "may":"Learn JS",
    "june":"Learn Security",
    "july":"Workout",
    "august":"PLay Game",
    "september":"Learn DB",
    "october":"<body style=background-color:grey><marquee><h1 style=color:white>Enjoy<h2>hello</h2></h1></marquee></body>",
    "november":"Learn QA",
    "december":"Get Job"

}

def index(request):
    list_items="" 
    months=list(monthly_challange.keys())

    for month in months:
        capitalized_month=month.capitalize()
        month_path=reverse("month-challange",args=[month])
        list_items+=f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)
        

    

# Create your views here.
def monthly_challanges_by_num(request,month):
    months=list(monthly_challange.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month=months[month-1]
    redirect_path=reverse("month-challange",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challanges(request,month):
    try:
        result=monthly_challange[month]
        return HttpResponse(f"<h1>{result}</h1>")
    except:
        return HttpResponseNotFound(render_to_string("challanges/challange.html")) 

def hello(request):
    hi=render_to_string("challanges/challange.html")
    return HttpResponse(hi)
