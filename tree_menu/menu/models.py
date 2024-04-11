from django.db import models


class MenuName(models.Model):
    name = models.CharField(unique=True, max_length=100)
    items = models.ManyToManyField('MenuItem', through='MenuNameItem', related_name='menu')

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
    item = models.ForeignKey(MenuItem, on_delete=models.deletion.CASCADE)
    level = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['pk', 'level']
