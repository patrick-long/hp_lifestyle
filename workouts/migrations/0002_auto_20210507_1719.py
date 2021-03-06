# Generated by Django 3.2.1 on 2021-05-07 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='exercise_name',
            field=models.CharField(default='my exercise', max_length=200),
        ),
        migrations.AddField(
            model_name='exercise',
            name='num_reps',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='exercise',
            name='num_sets',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='exercise',
            name='rest_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='exercise',
            name='weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='exercise',
            name='workout',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='workouts.workout'),
        ),
        migrations.AddField(
            model_name='workout',
            name='workout_name',
            field=models.CharField(default='my workout', max_length=300),
        ),
    ]
