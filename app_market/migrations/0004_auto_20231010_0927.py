# Generated by Django 3.0.5 on 2023-10-10 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_market', '0003_auto_20231009_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
