# Generated by Django 4.2.7 on 2024-01-25 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_remove_book_isborrowd_purcehase_history_isborrowd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purcehase_history',
            name='isBorrowd',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('★☆☆☆☆', 1), ('★★☆☆☆', 2), ('★★★☆☆', 3), ('★★★★☆', 4), ('★★★★★', 5)], max_length=50)),
                ('Book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
    ]
