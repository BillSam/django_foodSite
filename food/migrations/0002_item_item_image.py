# Generated by Django 3.1.7 on 2021-02-21 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://s3.amazonaws.com/ODNUploads/532dfdbcc6479placeholder_ food_item_2.png', max_length=500),
        ),
    ]
