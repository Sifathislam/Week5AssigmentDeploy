# Generated by Django 4.2.7 on 2024-01-26 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_publisherinfo_soldbookcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisherinfo',
            name='soldBookCount',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
    ]