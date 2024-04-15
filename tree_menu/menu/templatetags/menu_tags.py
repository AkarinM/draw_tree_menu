from django import template
import http.client

from menu.models import MenuName

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html')
def draw_menu(name_menu: str):
    menu = MenuName.objects.prefetch_related('items').filter(name=name_menu).first()
    print(menu.items)
    # for item in menu.items.filter(level=0):
    #     print(item)