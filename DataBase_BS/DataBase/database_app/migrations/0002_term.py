# Generated by Django 2.1.7 on 2019-04-11 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=15)),
            ],
        ),
    ]