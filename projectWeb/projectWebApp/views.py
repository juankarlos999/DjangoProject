"""File execute a function saludo include date"""
from datetime import datetime
from pyluach import dates
from django.shortcuts import render


def home(request):
    """
    Function that return principal page from web aplication
    """
    my_greeting = "Bienvenidos a todos"
    date_hebrew = dates.HebrewDate.today()
    date_utc = datetime.utcnow()
    dict_ctx = {"greeting": my_greeting, "Date_H":date_hebrew,\
        "Date_utc":date_utc}
    return render(request, 'index.html', dict_ctx)
