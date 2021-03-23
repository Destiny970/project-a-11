# Generated by Django 3.1.5 on 2021-03-21 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0012_auto_20210319_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='total_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='time_taken',
            field=models.CharField(choices=[('LESS_THAN_30', 'Quick Workout (Between 1-29 min)'), ('LESS_THAN_1_HR', 'Longer Workout (Between 30-59 min'), ('BETWEEN_1_AND_2_HRS', 'Long Workout (Between 60 and 119 min'), ('MORE_THAN_2_HRS', 'Very Long Workout (120 min or greater)')], default='LESS_THAN_30', max_length=20),
        ),
    ]
