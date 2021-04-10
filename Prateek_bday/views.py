from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def index(requests):
    birthday = datetime.datetime.now()
    return render(requests, "Birthday/index.html", {
        "birthday" : birthday.month == 4 and birthday.date == 17
    })