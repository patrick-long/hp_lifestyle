# Generated by Django 3.2.1 on 2021-05-08 21:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0005_alter_workout_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created'),
        ),
    ]
