from django.contrib import admin

from menu.models import MenuName, MenuItem


# admin.site.register(MenuName)


@admin.register(MenuName)
class MenuNameAdmin(admin.ModelAdmin):
    pass


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    pass
