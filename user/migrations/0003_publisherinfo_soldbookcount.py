# Generated by Django 4.2.7 on 2024-01-25 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_publisherinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisherinfo',
            name='soldBookCount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
