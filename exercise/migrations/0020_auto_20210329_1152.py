# Generated by Django 3.1.5 on 2021-03-29 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0019_exercise_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='location',
            field=models.CharField(choices=[('INSIDE', 'Indoors'), ('OUTSIDE', 'Outdoors')], default='INSIDE', max_length=7),
        ),
    ]
