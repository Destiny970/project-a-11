# Generated by Django 3.1.5 on 2021-04-18 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0028_auto_20210416_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='current_location',
            field=models.CharField(default='Charlottesville', max_length=50),
        ),
    ]