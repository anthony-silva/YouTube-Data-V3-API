# Generated by Django 3.1.2 on 2020-10-06 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_auto_20201006_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='channel_id',
            field=models.CharField(default=None, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='success',
            field=models.BooleanField(default=None),
        ),
    ]
