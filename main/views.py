from django.shortcuts import render_to_response
from django.template.loader import get_template
from .fucntions import MenuList


# Create your views here.
def StartPage(request):
    menu = MenuList()
    path = request.path

    return render_to_response("main/index.html", locals())


def AbouttPage(request):
    menu = MenuList()
    path = request.path
    about = [
        'Сотрудник 1',
        'Сотрудник 2',
        'Сотрудник 3',
    ]
    return render_to_response("main/about.html", locals())


def ContactsPage(request):
    menu = MenuList()
    path = request.path
    return render_to_response("main/contacts.html", locals())

def Auth(request):
    pass


def Registration(request):
    pass


