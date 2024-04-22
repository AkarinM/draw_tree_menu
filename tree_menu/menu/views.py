from django.db.models import Q
from django.shortcuts import render

from menu.models import MenuNameItem


# def draw_menu(request, menu_name: str, item_id: int, c_path: str):
def draw_menu(request, menu_name: str, c_path: str):
    resp_dict = dict()
    result_list = list()

    # pks_items = list(map(int, c_path.split('/')))
    pks_items = c_path.split('/')[:-1]

    # menu = MenuNameItem.objects.filter(Q(level__lte=c_level) | Q(level=c_level+1), menu__name=menu_name, pk=item_id).order_by('item__name')
    menu = list()

    query = MenuNameItem.objects.filter(Q(pk__in=pks_items) | Q(parent__in=pks_items) | Q(level=0), menu__name=menu_name)

    level = -1
    path = ''
    for i, m in enumerate(query):
        if level < m.level:
            pre = '<ul>'
            post = ''

            level = m.level
            path += '/' + str(m.pk) if path else str(m.pk)
        elif level > m.level:
            pre = ''
            post = ' '.join(
                ['</ul>'] * (level - m.level)
            )
            level = m.level
            path = '/'.join(path.split('/')[:-(level - m.level)])
        else:
            pre = ''
            post = ''

        menu.append(
            (pre, m, path + '/', post)
        )

    print(menu)

    return render(request, 'menu/draw_menu.html', {'menu': menu})



