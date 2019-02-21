from .models import MainMenu


def MenuList():
    menu_list = MainMenu.objects.all().order_by('order')

    return menu_list
