from django.db.models import Q
from django.shortcuts import render

from menu.models import MenuNameItem


# def draw_menu(request, menu_name: str, item_id: int, c_path: str):
def draw_menu(request, menu_name: str, c_path: str):
    resp_dict = dict()
    result_list = list()

    # pks_items = list(map(int, c_path.split('/')))
    pks_items = c_path.split('/')

    # menu = MenuNameItem.objects.filter(Q(level__lte=c_level) | Q(level=c_level+1), menu__name=menu_name, pk=item_id).order_by('item__name')
    menu = MenuNameItem.objects.filter(Q(pk__in=pks_items) | Q(parent=pks_items[-1]), menu__name=menu_name)

    return render(request, 'menu/menu.html', {})



