# Generated by Django 3.1.7 on 2021-02-27 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0004_auto_20210227_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='homework',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='uploads', to='panel.homework'),
        ),
        migrations.AlterField(
            model_name='upload',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='uploads', to=settings.AUTH_USER_MODEL),
        ),
    ]
