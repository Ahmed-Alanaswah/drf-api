# Generated by Django 4.0 on 2021-12-12 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
