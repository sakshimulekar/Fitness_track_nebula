# Generated by Django 4.2.4 on 2023-09-04 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_exercise_min'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='description',
            field=models.TextField(default='No description available', max_length=1000),
        ),
    ]
