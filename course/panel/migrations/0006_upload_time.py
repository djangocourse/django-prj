# Generated by Django 3.1.7 on 2021-02-27 16:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0005_auto_20210227_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='time',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
