# Generated by Django 4.2.3 on 2023-07-27 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shareRes', '0002_restaurant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='restaurant_like',
            new_name='restaurant_link',
        ),
    ]
