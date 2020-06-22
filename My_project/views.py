"""File execute a function saludo include date"""
from datetime import datetime
from pyluach import dates
from django.http import HttpResponse
from django.template import Template, Context


def msg_greeting(request):
    """Function that return principal page from web aplication"""

    my_path = "/home/juank/Github/DjangoProject/My_project/My_project/\
        templates/index.html"
    with open(''.join(my_path.split())) as index:
        my_greeting = "Bienvenidos a todos"
        date_hebrew = dates.HebrewDate.today()
        date_utc = datetime.utcnow()
        plt = Template(index.read())
        dict_ctx = {"greeting": my_greeting, "Date_H":date_hebrew,\
            "Date_utc":date_utc}
        ctx = Context(dict_ctx)
        doc_html = plt.render(ctx)
    return HttpResponse(doc_html)
