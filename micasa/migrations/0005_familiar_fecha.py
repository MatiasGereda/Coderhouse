# Generated by Django 4.1.3 on 2022-12-08 05:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('micasa', '0004_remove_familiar_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiar',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
