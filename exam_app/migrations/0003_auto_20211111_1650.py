# Generated by Django 3.2.8 on 2021-11-11 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0002_auction_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='auction',
            name='start_date',
            field=models.DateField(),
        ),
    ]