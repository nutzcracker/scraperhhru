# Generated by Django 4.0.6 on 2022-07-18 13:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
