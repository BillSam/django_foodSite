# Generated by Django 3.1.7 on 2021-02-21 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_auto_20210221_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='/home/work/Documents/pythhon/FooSite/food/static/food/media/default.jpg', max_length=500),
        ),
    ]
