# Generated by Django 3.1.5 on 2021-04-25 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0032_auto_20210422_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
