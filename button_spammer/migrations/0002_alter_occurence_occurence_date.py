# Generated by Django 4.2.6 on 2024-01-06 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('button_spammer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurence',
            name='occurence_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date field'),
        ),
    ]
