# Generated by Django 3.2 on 2021-04-27 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msg_events', '0016_alter_custommessage_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custommessage',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
