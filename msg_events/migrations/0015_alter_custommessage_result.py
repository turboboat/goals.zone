# Generated by Django 3.2 on 2021-04-27 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msg_events', '0014_custommessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custommessage',
            name='result',
            field=models.CharField(blank=True, default=None, max_length=2000),
        ),
    ]