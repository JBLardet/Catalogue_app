from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "sales_manager/index.html", context={"username": "évaluateur", "date": datetime.today()})


def login(request):
    return render(request, "sales_manager/login.html")
