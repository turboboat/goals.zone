# Generated by Django 3.0.3 on 2020-03-04 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0029_auto_20200304_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='priority',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
