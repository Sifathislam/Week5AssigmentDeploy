# Generated by Django 4.2.7 on 2023-12-31 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_category_alter_book_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='isBorrowd',
        ),
        migrations.AddField(
            model_name='purcehase_history',
            name='isBorrowd',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
