# Generated by Django 3.0.5 on 2020-05-30 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gyms', '0002_auto_20200527_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
