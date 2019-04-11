# Generated by Django 2.1.7 on 2019-04-09 00:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Log_info',
            fields=[
                ('user', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('number', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(default='上海大学宝山校区', max_length=50)),
                ('phone', models.CharField(default='00000000', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('number', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('credit', models.IntegerField(default=0)),
                ('class_hour', models.IntegerField(default=0)),
                ('college', models.ForeignKey(on_delete=False, to='database_app.College')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=15)),
                ('r_grade', models.IntegerField(null=True)),
                ('e_grade', models.IntegerField(null=True)),
                ('t_grade', models.IntegerField(null=True)),
                ('c_number', models.ForeignKey(on_delete=False, to='database_app.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Open',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=15)),
                ('time', models.CharField(max_length=10)),
                ('c_number', models.ForeignKey(on_delete=False, to='database_app.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=32)),
                ('birth', models.DateField(default=django.utils.timezone.now)),
                ('home_town', models.CharField(max_length=10)),
                ('phone', models.CharField(default='13000000000', max_length=15)),
                ('college', models.ForeignKey(on_delete=False, to='database_app.College')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Log_info',
            fields=[
                ('user', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('student_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=32)),
                ('birth', models.DateField(default=django.utils.timezone.now)),
                ('rank', models.CharField(default='讲师', max_length=10)),
                ('salary', models.IntegerField(default=0)),
                ('college', models.ForeignKey(on_delete=False, to='database_app.College')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_Log_info',
            fields=[
                ('user', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('teacher_no', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='open',
            name='t_number',
            field=models.ForeignKey(on_delete=False, to='database_app.Teacher'),
        ),
        migrations.AddField(
            model_name='mark',
            name='s_number',
            field=models.ForeignKey(on_delete=False, to='database_app.Student'),
        ),
        migrations.AddField(
            model_name='mark',
            name='t_number',
            field=models.ForeignKey(on_delete=False, to='database_app.Teacher'),
        ),
        migrations.AlterUniqueTogether(
            name='open',
            unique_together={('term', 'c_number', 't_number')},
        ),
        migrations.AlterUniqueTogether(
            name='mark',
            unique_together={('s_number', 'term', 'c_number', 't_number')},
        ),
    ]
