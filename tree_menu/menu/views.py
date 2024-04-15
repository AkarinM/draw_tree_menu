from django.shortcuts import render


def draw_menu(request, menu_name: str, item_id: int = None):


    return render(request, 'menu/menu.html', {})



