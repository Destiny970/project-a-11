# Generated by Django 3.1.6 on 2021-03-16 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0002_auto_20210315_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='exercise_date',
            field=models.DateTimeField(null=True, verbose_name='date completed'),
        ),
    ]