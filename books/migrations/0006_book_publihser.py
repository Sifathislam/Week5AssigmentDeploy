# Generated by Django 4.2.7 on 2024-01-25 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_publisherinfo'),
        ('books', '0005_book_isproduct_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publihser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.publisherinfo'),
        ),
    ]
