# Generated by Django 2.2 on 2019-04-22 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_app', '0002_term_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='open',
            name='al_sel',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='open',
            name='volume',
            field=models.IntegerField(default=50),
        ),
    ]
