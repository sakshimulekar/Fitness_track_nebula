# Generated by Django 4.2.4 on 2023-09-04 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_exercise_fitnessplan_customuser_trainer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='min',
            field=models.PositiveIntegerField(default=0),
        ),
    ]