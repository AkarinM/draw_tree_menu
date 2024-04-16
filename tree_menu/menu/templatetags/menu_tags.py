from django import template
import http.client

from menu.models import MenuName, MenuNameItem

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html')
def draw_menu(name_menu: str):
    menu = MenuNameItem.objects.filter(menu__name=name_menu, level=0).order_by('item__name')

    return {'menu': menu}
