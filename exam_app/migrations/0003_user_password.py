# Generated by Django 3.2.8 on 2021-11-12 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0002_auto_20211112_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='pass', max_length=16),
        ),
    ]
