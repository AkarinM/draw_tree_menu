# Generated by Django 5.0.4 on 2024-04-11 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuname',
            name='items',
            field=models.ManyToManyField(through='menu.MenuNameItem', to='menu.menuitem'),
        ),
    ]
