# Generated by Django 3.2.9 on 2021-11-08 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msg_events', '0019_auto_20211105_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='webhook',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
