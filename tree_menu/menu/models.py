from django.db import models


class MenuName(models.Model):
    name = models.CharField(unique=True, max_length=100)
    items = models.ManyToManyField('MenuItem', through='MenuNameItem', related_name='menu', through_fields=('menu', 'item'))

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.pk}: {self.name}'


class MenuItem(models.Model):
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.pk}: {self.name}'


class MenuNameItem(models.Model):
    menu = models.ForeignKey(MenuName, on_delete=models.deletion.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.deletion.CASCADE, related_name='menu_name_items_item')
    level = models.PositiveIntegerField(default=0)
    parent = models.ForeignKey(MenuItem, on_delete=models.deletion.CASCADE, related_name='menu_name_items_parent', null=True)

    class Meta:
        ordering = ['pk', 'level']

    def __str__(self):
        return f'{self.menu.name}/{self.item.name}|lvl:{self.level}'
