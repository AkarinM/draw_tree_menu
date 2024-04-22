from django import template
import http.client

from menu.models import MenuName, MenuNameItem

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html')
def draw_menu(name_menu: str):
    menu = list()

    query = MenuNameItem.objects.select_related('menu', 'item').filter(menu__name=name_menu, level=0)

    for i, m in enumerate(query):
        if i == 0:
            pre = '<ul>'
            post = ''
        elif i == len(query) - 1:
            pre = ''
            post = '</ul>'
        else:
            pre = ''
            post = ''

        menu.append(
            (pre, m, str(m.pk) + '/', post)
        )

    return {'menu': menu}
