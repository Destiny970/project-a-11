# Generated by Django 3.1.5 on 2021-03-22 23:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_type', models.CharField(choices=[('CAR', 'cardio'), ('STR', 'strength'), ('SPT', 'sports'), ('FLX', 'yoga/flexibility')], default='CAR', max_length=3)),
                ('exercise_date', models.DateTimeField(null=True, verbose_name='date completed')),
                ('time_taken', models.CharField(choices=[('LESS_THAN_30', 'Quick Workout (Between 1-29 min)'), ('LESS_THAN_1_HR', 'Longer Workout (Between 30-59 min'), ('BETWEEN_1_AND_2_HRS', 'Long Workout (Between 60 and 119 min'), ('MORE_THAN_2_HRS', 'Very Long Workout (120 min or greater)')], default='LESS_THAN_30', max_length=20)),
                ('points', models.IntegerField(default=0)),
                ('description', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
