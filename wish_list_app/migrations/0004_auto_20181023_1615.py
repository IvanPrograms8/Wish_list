# Generated by Django 2.1.2 on 2018-10-23 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wish_list_app', '0003_remove_wish_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
